import time
from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.agent_run import AgentRun
from app.models.agent_suggestion import AgentSuggestion
from app.models.tool_call import ToolCall


def plan_task(task: Task, task_context: str, db: Session) -> AgentRun:
    """
    Rule-based Planning Agent that generates subtask suggestions.
    For V1, this is a simulated agent that creates structured suggestions
    based on the task title and description.
    """
    start_time = time.time()
    
    # Create agent run record
    agent_run = AgentRun(
        project_id=task.project_id,
        task_id=task.id,
        agent_type="planning",
        status="running",
        input=f"Task: {task.title}\nDescription: {task.description or 'None'}\nContext: {task_context or 'None'}"
    )
    db.add(agent_run)
    db.commit()
    db.refresh(agent_run)
    
    try:
        # Rule-based subtask generation
        suggestions = generate_subtask_suggestions(task, task_context)
        
        # Create suggestion records
        for idx, suggestion in enumerate(suggestions, 1):
            agent_suggestion = AgentSuggestion(
                agent_run_id=agent_run.id,
                suggestion_type="subtask",
                title=suggestion["title"],
                description=suggestion.get("description"),
                status="pending"
            )
            db.add(agent_suggestion)
        
        # Create simulated tool call records (for traceability)
        tool_call = ToolCall(
            agent_run_id=agent_run.id,
            tool_type="local_tool",
            tool_name="rule_based_planner",
            request_summary=f"Analyze task: {task.title[:100]}",
            response_summary=f"Generated {len(suggestions)} subtask suggestions",
            status="success"
        )
        db.add(tool_call)
        
        # Update agent run status
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        
        agent_run.status = "completed"
        agent_run.output = f"Successfully generated {len(suggestions)} subtask suggestions for review."
        agent_run.duration_ms = duration_ms
        
        db.commit()
        db.refresh(agent_run)
        
        return agent_run
        
    except Exception as e:
        # Handle errors
        end_time = time.time()
        duration_ms = int((end_time - start_time) * 1000)
        
        agent_run.status = "failed"
        agent_run.error = str(e)
        agent_run.duration_ms = duration_ms
        
        db.commit()
        db.refresh(agent_run)
        
        raise


def generate_subtask_suggestions(task: Task, context: str) -> list:
    """
    Generate rule-based subtask suggestions.
    This is a simple implementation that creates structured subtasks
    based on common software development patterns.
    """
    suggestions = []
    task_lower = task.title.lower()
    
    # Check for common patterns in task title
    if any(word in task_lower for word in ["implement", "build", "create", "develop", "add"]):
        suggestions.extend([
            {
                "title": f"Research and design approach for: {task.title}",
                "description": "Investigate requirements, technical constraints, and design the implementation approach."
            },
            {
                "title": f"Implement core functionality for: {task.title}",
                "description": "Write the main implementation code following the design."
            },
            {
                "title": f"Write tests for: {task.title}",
                "description": "Create unit and integration tests to verify the implementation."
            },
            {
                "title": f"Document and review: {task.title}",
                "description": "Add documentation and conduct code review before completion."
            }
        ])
    elif any(word in task_lower for word in ["fix", "bug", "issue", "error"]):
        suggestions.extend([
            {
                "title": f"Reproduce and diagnose: {task.title}",
                "description": "Create a reproducible test case and identify the root cause."
            },
            {
                "title": f"Implement fix for: {task.title}",
                "description": "Apply the fix and verify it resolves the issue."
            },
            {
                "title": f"Add regression test for: {task.title}",
                "description": "Create test coverage to prevent this issue from recurring."
            }
        ])
    elif any(word in task_lower for word in ["refactor", "improve", "optimize"]):
        suggestions.extend([
            {
                "title": f"Analyze current implementation: {task.title}",
                "description": "Review existing code and identify improvement opportunities."
            },
            {
                "title": f"Refactor code for: {task.title}",
                "description": "Make the improvements while maintaining functionality."
            },
            {
                "title": f"Verify no regressions: {task.title}",
                "description": "Run all tests to ensure existing functionality is preserved."
            }
        ])
    else:
        # Generic fallback structure
        suggestions.extend([
            {
                "title": f"Plan and prepare: {task.title}",
                "description": "Break down the task into specific action items and gather requirements."
            },
            {
                "title": f"Execute main work: {task.title}",
                "description": "Complete the primary deliverables for this task."
            },
            {
                "title": f"Review and finalize: {task.title}",
                "description": "Verify completion and document outcomes."
            }
        ])
    
    # If context is provided, add a context-specific suggestion
    if context and len(context.strip()) > 10:
        suggestions.insert(0, {
            "title": f"Review context and requirements: {task.title}",
            "description": f"Consider the provided context: {context[:200]}..."
        })
    
    return suggestions[:5]  # Limit to 5 suggestions
