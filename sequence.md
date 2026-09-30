# ProjectFlow AI - Main User Journey Sequence Diagram

```drawio
<mxfile>
  <diagram id="kRuMwJ7LU0wxGpnAAj2F" name="Page-1">
    <mxGraphModel dx="1300" dy="1237" grid="1" gridSize="10" guides="1" tooltips="0" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="nThWUC4bMk5yji6sOE_n-0" />
        <mxCell id="nThWUC4bMk5yji6sOE_n-1" parent="nThWUC4bMk5yji6sOE_n-0" />
        <UserObject label="" mermaidData="{&#xa;  &quot;data&quot;: &quot;sequenceDiagram\n    participant User\n    participant Frontend\n    participant Backend\n    participant Database\n\n    Note over User,Database: 1. Open Projects\n    User-&gt;&gt;Frontend: Navigate to Projects\n    Frontend-&gt;&gt;Backend: GET /projects\n    Backend-&gt;&gt;Database: Query projects for user\n    Database--&gt;&gt;Backend: Return projects\n    Backend-&gt;&gt;Database: Calculate task counts\n    Database--&gt;&gt;Backend: Return task data\n    Backend--&gt;&gt;Frontend: Return projects with counts\n    Frontend--&gt;&gt;User: Display projects table\n\n    Note over User,Database: 2. Create Project\n    User-&gt;&gt;Frontend: Click \&quot;New Project\&quot;\n    Frontend-&gt;&gt;User: Show Add/Edit Project form\n    User-&gt;&gt;Frontend: Enter name, description, status\n    User-&gt;&gt;Frontend: Click \&quot;Create Project\&quot;\n    Frontend-&gt;&gt;Backend: POST /projects\n    Backend-&gt;&gt;Database: Insert new project\n    Database--&gt;&gt;Backend: Return created project\n    Backend--&gt;&gt;Frontend: Return project\n    Frontend-&gt;&gt;User: Navigate to Project Detail\n\n    Note over User,Database: 3. Add Tasks\n    User-&gt;&gt;Frontend: Click \&quot;Add Task\&quot;\n    Frontend-&gt;&gt;User: Show Add/Edit Task form\n    User-&gt;&gt;Frontend: Enter title, description, priority, status, due date\n    User-&gt;&gt;Frontend: Click \&quot;Create Task\&quot;\n    Frontend-&gt;&gt;Backend: POST /projects/{project_id}/tasks\n    Backend-&gt;&gt;Database: Verify project ownership\n    Database--&gt;&gt;Backend: Return project\n    Backend-&gt;&gt;Database: Insert new task\n    Database--&gt;&gt;Backend: Return created task\n    Backend--&gt;&gt;Frontend: Return task\n    Frontend-&gt;&gt;User: Navigate to Task Detail\n\n    Note over User,Database: 4. Update Status/Priority\n    User-&gt;&gt;Frontend: Click \&quot;Edit Task\&quot;\n    Frontend-&gt;&gt;User: Show edit form with current values\n    User-&gt;&gt;Frontend: Update status and/or priority\n    User-&gt;&gt;Frontend: Click \&quot;Save Changes\&quot;\n    Frontend-&gt;&gt;Backend: PUT /tasks/{task_id}\n    Backend-&gt;&gt;Database: Verify ownership via project\n    Database--&gt;&gt;Backend: Return task and project\n    Backend-&gt;&gt;Database: Update task fields\n    Database--&gt;&gt;Backend: Return updated task\n    Backend--&gt;&gt;Frontend: Return task\n    Frontend-&gt;&gt;User: Navigate to Task Detail\n\n    Note over User,Database: 5. Open Task\n    User-&gt;&gt;Frontend: Navigate back to Project Detail\n    Frontend-&gt;&gt;Backend: GET /projects/{project_id}/tasks\n    Backend-&gt;&gt;Database: Verify project ownership\n    Database--&gt;&gt;Backend: Return project\n    Backend-&gt;&gt;Database: Query tasks with filters\n    Database--&gt;&gt;Backend: Return tasks\n    Backend--&gt;&gt;Frontend: Return tasks\n    Frontend--&gt;&gt;User: Display tasks table\n    User-&gt;&gt;Frontend: Click on task row\n    Frontend-&gt;&gt;Backend: GET /tasks/{task_id}\n    Backend-&gt;&gt;Database: Query task, subtasks, agent runs\n    Database--&gt;&gt;Backend: Return task details\n    Backend--&gt;&gt;Frontend: Return task with subtasks and agent runs\n    Frontend--&gt;&gt;User: Display Task Detail\n\n    Note over User,Database: 6. Ask Planning Agent for Subtasks\n    User-&gt;&gt;Frontend: Click \&quot;Plan with AI\&quot;\n    Frontend-&gt;&gt;User: Show context input (optional)\n    User-&gt;&gt;Frontend: Click \&quot;Generate Plan\&quot;\n    Frontend-&gt;&gt;Backend: POST /tasks/{task_id}/plan\n    Backend-&gt;&gt;Database: Verify task ownership\n    Database--&gt;&gt;Backend: Return task and project\n    Backend-&gt;&gt;Backend: Invoke Planning Agent\n    Backend-&gt;&gt;Database: Create agent_run record\n    Database--&gt;&gt;Backend: Return agent_run\n    Backend-&gt;&gt;Database: Insert agent_suggestions\n    Database--&gt;&gt;Backend: Return suggestions\n    Backend--&gt;&gt;Frontend: Return agent_run_id and suggestions\n    Frontend-&gt;&gt;User: Navigate to AI Plan Review\n\n    Note over User,Database: 7. Review and Accept Selected Suggestions\n    User-&gt;&gt;Frontend: View suggested subtasks\n    Frontend-&gt;&gt;Backend: GET /agent-runs/{agent_run_id}\n    Backend-&gt;&gt;Database: Query agent run details\n    Database--&gt;&gt;Backend: Return run, suggestions, tool_calls\n    Backend--&gt;&gt;Frontend: Return agent run details\n    Frontend--&gt;&gt;User: Display suggestions with checkboxes\n    User-&gt;&gt;Frontend: Select desired suggestions\n    User-&gt;&gt;Frontend: Click \&quot;Accept Selected\&quot;\n    Frontend-&gt;&gt;Backend: POST /agent-runs/{agent_run_id}/accept\n    Backend-&gt;&gt;Database: Verify ownership\n    Database--&gt;&gt;Backend: Return agent run and project\n    Backend-&gt;&gt;Database: Query selected suggestions\n    Database--&gt;&gt;Backend: Return suggestions\n    Backend-&gt;&gt;Database: Create subtasks from suggestions\n    Database--&gt;&gt;Backend: Return created subtasks\n    Backend-&gt;&gt;Database: Update suggestion status to \&quot;accepted\&quot;\n    Database--&gt;&gt;Backend: Confirm update\n    Backend--&gt;&gt;Frontend: Return created subtasks\n    Frontend-&gt;&gt;User: Navigate back to Task Detail\n    Frontend-&gt;&gt;Backend: GET /tasks/{task_id}\n    Backend-&gt;&gt;Database: Query task with new subtasks\n    Database--&gt;&gt;Backend: Return task details\n    Backend--&gt;&gt;Frontend: Return task with subtasks\n    Frontend--&gt;&gt;User: Display task with accepted subtasks\n\n    Note over User,Database: 8. Inspect Agent Runs/Tool Calls\n    User-&gt;&gt;Frontend: Navigate to Agent Runs\n    Frontend-&gt;&gt;Backend: GET /agent-runs\n    Backend-&gt;&gt;Database: Query user&#39;s projects\n    Database--&gt;&gt;Backend: Return project IDs\n    Backend-&gt;&gt;Database: Query agent runs with filters\n    Database--&gt;&gt;Backend: Return agent runs\n    Backend--&gt;&gt;Frontend: Return agent run history\n    Frontend--&gt;&gt;User: Display agent run table\n    User-&gt;&gt;Frontend: Click \&quot;View Run\&quot;\n    Frontend-&gt;&gt;Backend: GET /agent-runs/{agent_run_id}\n    Backend-&gt;&gt;Database: Query agent run details\n    Database--&gt;&gt;Backend: Return run, suggestions, tool_calls\n    Backend--&gt;&gt;Frontend: Return agent run detail\n    Frontend--&gt;&gt;User: Display run input, output, timing, tool calls\n\n    Note over User,Database: 9. Connect GitHub MCP Integration (Later)\n    User-&gt;&gt;Frontend: Navigate to Integrations\n    Frontend-&gt;&gt;Backend: GET /integrations\n    Backend-&gt;&gt;Database: Query integrations\n    Database--&gt;&gt;Backend: Return integrations\n    Backend--&gt;&gt;Frontend: Return integrations\n    Frontend--&gt;&gt;User: Display connections table\n    User-&gt;&gt;Frontend: Click \&quot;Connect GitHub MCP\&quot;\n    User-&gt;&gt;Frontend: Provide configuration reference\n    Frontend-&gt;&gt;Backend: POST /integrations/github-mcp/connect\n    Backend-&gt;&gt;Backend: Validate MCP configuration\n    Backend-&gt;&gt;Database: Insert integration record\n    Database--&gt;&gt;Backend: Return integration\n    Backend--&gt;&gt;Frontend: Return connection status\n    Frontend--&gt;&gt;User: Display updated integrations&quot;,&#xa;  &quot;config&quot;: null&#xa;}" id="oOSgu5qEeW-CKJ_P9lIY-0">
          <mxCell connectable="0" parent="nThWUC4bMk5yji6sOE_n-1" style="group;transparentBounds=1;editIcon=1;lockedGroup=0;groupPadding=10;" vertex="1">
            <mxGeometry as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="User" mermaidId="n:User" mermaidBaseStyle="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="User" id="nThWUC4bMk5yji6sOE_n-2">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="5912" width="150" x="10" y="10" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="Frontend" mermaidId="n:Frontend" mermaidBaseStyle="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="Frontend" id="nThWUC4bMk5yji6sOE_n-3">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="5912" width="150" x="415" y="10" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="Backend" mermaidId="n:Backend" mermaidBaseStyle="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="Backend" id="nThWUC4bMk5yji6sOE_n-4">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="5912" width="150" x="762" y="10" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="Database" mermaidId="n:Database" mermaidBaseStyle="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="Database" id="nThWUC4bMk5yji6sOE_n-5">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;container=1;dropTarget=0;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;newEdgeStyle={&quot;edgeStyle&quot;:&quot;elbowEdgeStyle&quot;,&quot;elbow&quot;:&quot;vertical&quot;,&quot;curved&quot;:0,&quot;rounded&quot;:0};lifelineDashed=0;strokeWidth=2;rounded=1;absoluteArcSize=1;arcSize=6;lifelineColor=light-dark(#9370DB,#cccccc);size=65;lifelineMirror=1;fillColor=light-dark(#ECECFF,#1f2020);strokeColor=light-dark(#9370DB,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="5912" width="150" x="1092" y="10" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Projects" mermaidId="e:User-&gt;Frontend#0" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Projects" id="nThWUC4bMk5yji6sOE_n-6">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="169" />
              </Array>
              <mxPoint x="85" y="169" as="sourcePoint" />
              <mxPoint x="490" y="169" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /projects" mermaidId="e:Frontend-&gt;Backend#0" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /projects" id="nThWUC4bMk5yji6sOE_n-7">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="213" />
              </Array>
              <mxPoint x="490" y="213" as="sourcePoint" />
              <mxPoint x="837" y="213" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query projects for user" mermaidId="e:Backend-&gt;Database#0" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query projects for user" id="nThWUC4bMk5yji6sOE_n-8">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="257" />
              </Array>
              <mxPoint x="837" y="257" as="sourcePoint" />
              <mxPoint x="1167" y="257" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return projects" mermaidId="e:Database-&gt;Backend#0" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return projects" id="nThWUC4bMk5yji6sOE_n-9">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="301" />
              </Array>
              <mxPoint x="1167" y="301" as="sourcePoint" />
              <mxPoint x="837" y="301" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Calculate task counts" mermaidId="e:Backend-&gt;Database#1" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Calculate task counts" id="nThWUC4bMk5yji6sOE_n-10">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="345" />
              </Array>
              <mxPoint x="837" y="345" as="sourcePoint" />
              <mxPoint x="1167" y="345" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task data" mermaidId="e:Database-&gt;Backend#1" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task data" id="nThWUC4bMk5yji6sOE_n-11">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="389" />
              </Array>
              <mxPoint x="1167" y="389" as="sourcePoint" />
              <mxPoint x="837" y="389" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return projects with counts" mermaidId="e:Backend-&gt;Frontend#0" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return projects with counts" id="nThWUC4bMk5yji6sOE_n-12">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="433" />
              </Array>
              <mxPoint x="837" y="433" as="sourcePoint" />
              <mxPoint x="490" y="433" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display projects table" mermaidId="e:Frontend-&gt;User#0" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display projects table" id="nThWUC4bMk5yji6sOE_n-13">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="477" />
              </Array>
              <mxPoint x="490" y="477" as="sourcePoint" />
              <mxPoint x="85" y="477" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;New Project&quot;" mermaidId="e:User-&gt;Frontend#1" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;New Project&quot;" id="nThWUC4bMk5yji6sOE_n-14">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="571" />
              </Array>
              <mxPoint x="85" y="571" as="sourcePoint" />
              <mxPoint x="490" y="571" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Show Add/Edit Project form" mermaidId="e:Frontend-&gt;User#1" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Show Add/Edit Project form" id="nThWUC4bMk5yji6sOE_n-15">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="615" />
              </Array>
              <mxPoint x="490" y="615" as="sourcePoint" />
              <mxPoint x="85" y="615" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Enter name, description, status" mermaidId="e:User-&gt;Frontend#2" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Enter name, description, status" id="nThWUC4bMk5yji6sOE_n-16">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="659" />
              </Array>
              <mxPoint x="85" y="659" as="sourcePoint" />
              <mxPoint x="490" y="659" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Create Project&quot;" mermaidId="e:User-&gt;Frontend#3" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Create Project&quot;" id="nThWUC4bMk5yji6sOE_n-17">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="703" />
              </Array>
              <mxPoint x="85" y="703" as="sourcePoint" />
              <mxPoint x="490" y="703" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="POST /projects" mermaidId="e:Frontend-&gt;Backend#1" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="POST /projects" id="nThWUC4bMk5yji6sOE_n-18">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="747" />
              </Array>
              <mxPoint x="490" y="747" as="sourcePoint" />
              <mxPoint x="837" y="747" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Insert new project" mermaidId="e:Backend-&gt;Database#2" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Insert new project" id="nThWUC4bMk5yji6sOE_n-19">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="791" />
              </Array>
              <mxPoint x="837" y="791" as="sourcePoint" />
              <mxPoint x="1167" y="791" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return created project" mermaidId="e:Database-&gt;Backend#2" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return created project" id="nThWUC4bMk5yji6sOE_n-20">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="835" />
              </Array>
              <mxPoint x="1167" y="835" as="sourcePoint" />
              <mxPoint x="837" y="835" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return project" mermaidId="e:Backend-&gt;Frontend#1" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return project" id="nThWUC4bMk5yji6sOE_n-21">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="879" />
              </Array>
              <mxPoint x="837" y="879" as="sourcePoint" />
              <mxPoint x="490" y="879" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Project Detail" mermaidId="e:Frontend-&gt;User#2" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Project Detail" id="nThWUC4bMk5yji6sOE_n-22">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="923" />
              </Array>
              <mxPoint x="490" y="923" as="sourcePoint" />
              <mxPoint x="85" y="923" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Add Task&quot;" mermaidId="e:User-&gt;Frontend#4" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Add Task&quot;" id="nThWUC4bMk5yji6sOE_n-23">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1017" />
              </Array>
              <mxPoint x="85" y="1017" as="sourcePoint" />
              <mxPoint x="490" y="1017" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Show Add/Edit Task form" mermaidId="e:Frontend-&gt;User#3" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Show Add/Edit Task form" id="nThWUC4bMk5yji6sOE_n-24">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1061" />
              </Array>
              <mxPoint x="490" y="1061" as="sourcePoint" />
              <mxPoint x="85" y="1061" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Enter title, description, priority, status, due date" mermaidId="e:User-&gt;Frontend#5" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Enter title, description, priority, status, due date" id="nThWUC4bMk5yji6sOE_n-25">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1105" />
              </Array>
              <mxPoint x="85" y="1105" as="sourcePoint" />
              <mxPoint x="490" y="1105" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Create Task&quot;" mermaidId="e:User-&gt;Frontend#6" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Create Task&quot;" id="nThWUC4bMk5yji6sOE_n-26">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1149" />
              </Array>
              <mxPoint x="85" y="1149" as="sourcePoint" />
              <mxPoint x="490" y="1149" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="POST /projects/{project_id}/tasks" mermaidId="e:Frontend-&gt;Backend#2" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="POST /projects/{project_id}/tasks" id="nThWUC4bMk5yji6sOE_n-27">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="1193" />
              </Array>
              <mxPoint x="490" y="1193" as="sourcePoint" />
              <mxPoint x="837" y="1193" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Verify project ownership" mermaidId="e:Backend-&gt;Database#3" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Verify project ownership" id="nThWUC4bMk5yji6sOE_n-28">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1237" />
              </Array>
              <mxPoint x="837" y="1237" as="sourcePoint" />
              <mxPoint x="1167" y="1237" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return project" mermaidId="e:Database-&gt;Backend#3" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return project" id="nThWUC4bMk5yji6sOE_n-29">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1281" />
              </Array>
              <mxPoint x="1167" y="1281" as="sourcePoint" />
              <mxPoint x="837" y="1281" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Insert new task" mermaidId="e:Backend-&gt;Database#4" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Insert new task" id="nThWUC4bMk5yji6sOE_n-30">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1325" />
              </Array>
              <mxPoint x="837" y="1325" as="sourcePoint" />
              <mxPoint x="1167" y="1325" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return created task" mermaidId="e:Database-&gt;Backend#4" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return created task" id="nThWUC4bMk5yji6sOE_n-31">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1369" />
              </Array>
              <mxPoint x="1167" y="1369" as="sourcePoint" />
              <mxPoint x="837" y="1369" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task" mermaidId="e:Backend-&gt;Frontend#2" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task" id="nThWUC4bMk5yji6sOE_n-32">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="1413" />
              </Array>
              <mxPoint x="837" y="1413" as="sourcePoint" />
              <mxPoint x="490" y="1413" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Task Detail" mermaidId="e:Frontend-&gt;User#4" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Task Detail" id="nThWUC4bMk5yji6sOE_n-33">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1457" />
              </Array>
              <mxPoint x="490" y="1457" as="sourcePoint" />
              <mxPoint x="85" y="1457" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Edit Task&quot;" mermaidId="e:User-&gt;Frontend#7" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Edit Task&quot;" id="nThWUC4bMk5yji6sOE_n-34">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1551" />
              </Array>
              <mxPoint x="85" y="1551" as="sourcePoint" />
              <mxPoint x="490" y="1551" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Show edit form with current values" mermaidId="e:Frontend-&gt;User#5" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Show edit form with current values" id="nThWUC4bMk5yji6sOE_n-35">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1595" />
              </Array>
              <mxPoint x="490" y="1595" as="sourcePoint" />
              <mxPoint x="85" y="1595" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Update status and/or priority" mermaidId="e:User-&gt;Frontend#8" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Update status and/or priority" id="nThWUC4bMk5yji6sOE_n-36">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1639" />
              </Array>
              <mxPoint x="85" y="1639" as="sourcePoint" />
              <mxPoint x="490" y="1639" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Save Changes&quot;" mermaidId="e:User-&gt;Frontend#9" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Save Changes&quot;" id="nThWUC4bMk5yji6sOE_n-37">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1683" />
              </Array>
              <mxPoint x="85" y="1683" as="sourcePoint" />
              <mxPoint x="490" y="1683" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="PUT /tasks/{task_id}" mermaidId="e:Frontend-&gt;Backend#3" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="PUT /tasks/{task_id}" id="nThWUC4bMk5yji6sOE_n-38">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="1727" />
              </Array>
              <mxPoint x="490" y="1727" as="sourcePoint" />
              <mxPoint x="837" y="1727" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Verify ownership via project" mermaidId="e:Backend-&gt;Database#5" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Verify ownership via project" id="nThWUC4bMk5yji6sOE_n-39">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1771" />
              </Array>
              <mxPoint x="837" y="1771" as="sourcePoint" />
              <mxPoint x="1167" y="1771" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task and project" mermaidId="e:Database-&gt;Backend#5" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task and project" id="nThWUC4bMk5yji6sOE_n-40">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1815" />
              </Array>
              <mxPoint x="1167" y="1815" as="sourcePoint" />
              <mxPoint x="837" y="1815" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Update task fields" mermaidId="e:Backend-&gt;Database#6" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Update task fields" id="nThWUC4bMk5yji6sOE_n-41">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1859" />
              </Array>
              <mxPoint x="837" y="1859" as="sourcePoint" />
              <mxPoint x="1167" y="1859" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return updated task" mermaidId="e:Database-&gt;Backend#6" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return updated task" id="nThWUC4bMk5yji6sOE_n-42">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="1903" />
              </Array>
              <mxPoint x="1167" y="1903" as="sourcePoint" />
              <mxPoint x="837" y="1903" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task" mermaidId="e:Backend-&gt;Frontend#3" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task" id="nThWUC4bMk5yji6sOE_n-43">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="1947" />
              </Array>
              <mxPoint x="837" y="1947" as="sourcePoint" />
              <mxPoint x="490" y="1947" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Task Detail" mermaidId="e:Frontend-&gt;User#6" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Task Detail" id="nThWUC4bMk5yji6sOE_n-44">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="1991" />
              </Array>
              <mxPoint x="490" y="1991" as="sourcePoint" />
              <mxPoint x="85" y="1991" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate back to Project Detail" mermaidId="e:User-&gt;Frontend#10" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate back to Project Detail" id="nThWUC4bMk5yji6sOE_n-45">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2085" />
              </Array>
              <mxPoint x="85" y="2085" as="sourcePoint" />
              <mxPoint x="490" y="2085" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /projects/{project_id}/tasks" mermaidId="e:Frontend-&gt;Backend#4" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /projects/{project_id}/tasks" id="nThWUC4bMk5yji6sOE_n-46">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="2129" />
              </Array>
              <mxPoint x="490" y="2129" as="sourcePoint" />
              <mxPoint x="837" y="2129" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Verify project ownership" mermaidId="e:Backend-&gt;Database#7" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Verify project ownership" id="nThWUC4bMk5yji6sOE_n-47">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2173" />
              </Array>
              <mxPoint x="837" y="2173" as="sourcePoint" />
              <mxPoint x="1167" y="2173" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return project" mermaidId="e:Database-&gt;Backend#7" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return project" id="nThWUC4bMk5yji6sOE_n-48">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2217" />
              </Array>
              <mxPoint x="1167" y="2217" as="sourcePoint" />
              <mxPoint x="837" y="2217" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query tasks with filters" mermaidId="e:Backend-&gt;Database#8" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query tasks with filters" id="nThWUC4bMk5yji6sOE_n-49">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2261" />
              </Array>
              <mxPoint x="837" y="2261" as="sourcePoint" />
              <mxPoint x="1167" y="2261" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return tasks" mermaidId="e:Database-&gt;Backend#8" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return tasks" id="nThWUC4bMk5yji6sOE_n-50">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2305" />
              </Array>
              <mxPoint x="1167" y="2305" as="sourcePoint" />
              <mxPoint x="837" y="2305" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return tasks" mermaidId="e:Backend-&gt;Frontend#4" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return tasks" id="nThWUC4bMk5yji6sOE_n-51">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="2349" />
              </Array>
              <mxPoint x="837" y="2349" as="sourcePoint" />
              <mxPoint x="490" y="2349" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display tasks table" mermaidId="e:Frontend-&gt;User#7" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display tasks table" id="nThWUC4bMk5yji6sOE_n-52">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2393" />
              </Array>
              <mxPoint x="490" y="2393" as="sourcePoint" />
              <mxPoint x="85" y="2393" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click on task row" mermaidId="e:User-&gt;Frontend#11" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click on task row" id="nThWUC4bMk5yji6sOE_n-53">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2437" />
              </Array>
              <mxPoint x="85" y="2437" as="sourcePoint" />
              <mxPoint x="490" y="2437" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /tasks/{task_id}" mermaidId="e:Frontend-&gt;Backend#5" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /tasks/{task_id}" id="nThWUC4bMk5yji6sOE_n-54">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="2481" />
              </Array>
              <mxPoint x="490" y="2481" as="sourcePoint" />
              <mxPoint x="837" y="2481" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query task, subtasks, agent runs" mermaidId="e:Backend-&gt;Database#9" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query task, subtasks, agent runs" id="nThWUC4bMk5yji6sOE_n-55">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2525" />
              </Array>
              <mxPoint x="837" y="2525" as="sourcePoint" />
              <mxPoint x="1167" y="2525" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task details" mermaidId="e:Database-&gt;Backend#9" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task details" id="nThWUC4bMk5yji6sOE_n-56">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2569" />
              </Array>
              <mxPoint x="1167" y="2569" as="sourcePoint" />
              <mxPoint x="837" y="2569" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task with subtasks and agent runs" mermaidId="e:Backend-&gt;Frontend#5" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task with subtasks and agent runs" id="nThWUC4bMk5yji6sOE_n-57">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="2613" />
              </Array>
              <mxPoint x="837" y="2613" as="sourcePoint" />
              <mxPoint x="490" y="2613" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display Task Detail" mermaidId="e:Frontend-&gt;User#8" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display Task Detail" id="nThWUC4bMk5yji6sOE_n-58">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2657" />
              </Array>
              <mxPoint x="490" y="2657" as="sourcePoint" />
              <mxPoint x="85" y="2657" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Plan with AI&quot;" mermaidId="e:User-&gt;Frontend#12" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Plan with AI&quot;" id="nThWUC4bMk5yji6sOE_n-59">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2751" />
              </Array>
              <mxPoint x="85" y="2751" as="sourcePoint" />
              <mxPoint x="490" y="2751" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Show context input (optional)" mermaidId="e:Frontend-&gt;User#9" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Show context input (optional)" id="nThWUC4bMk5yji6sOE_n-60">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2795" />
              </Array>
              <mxPoint x="490" y="2795" as="sourcePoint" />
              <mxPoint x="85" y="2795" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Generate Plan&quot;" mermaidId="e:User-&gt;Frontend#13" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Generate Plan&quot;" id="nThWUC4bMk5yji6sOE_n-61">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="2839" />
              </Array>
              <mxPoint x="85" y="2839" as="sourcePoint" />
              <mxPoint x="490" y="2839" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="POST /tasks/{task_id}/plan" mermaidId="e:Frontend-&gt;Backend#6" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="POST /tasks/{task_id}/plan" id="nThWUC4bMk5yji6sOE_n-62">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="2883" />
              </Array>
              <mxPoint x="490" y="2883" as="sourcePoint" />
              <mxPoint x="837" y="2883" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Verify task ownership" mermaidId="e:Backend-&gt;Database#10" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Verify task ownership" id="nThWUC4bMk5yji6sOE_n-63">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2927" />
              </Array>
              <mxPoint x="837" y="2927" as="sourcePoint" />
              <mxPoint x="1167" y="2927" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task and project" mermaidId="e:Database-&gt;Backend#10" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task and project" id="nThWUC4bMk5yji6sOE_n-64">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="2971" />
              </Array>
              <mxPoint x="1167" y="2971" as="sourcePoint" />
              <mxPoint x="837" y="2971" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="" mermaidId="e:Backend-&gt;Backend#0" mermaidBaseStyle="edgeStyle=none;curved=1;endArrow=block;endSize=9;verticalAlign=bottom;align=center;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="" id="nThWUC4bMk5yji6sOE_n-65">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="edgeStyle=none;curved=1;endArrow=block;endSize=9;verticalAlign=bottom;align=center;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="872" y="3045" />
                <mxPoint x="876" y="3057" />
                <mxPoint x="872" y="3069" />
              </Array>
              <mxPoint x="837" y="3045" as="sourcePoint" />
              <mxPoint x="837" y="3069" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <mxCell id="nThWUC4bMk5yji6sOE_n-66" parent="oOSgu5qEeW-CKJ_P9lIY-0" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;fontColor=light-dark(#333333,#cccccc);" value="Invoke Planning Agent" vertex="1">
          <mxGeometry height="18" width="200" x="737" y="3021" as="geometry" />
        </mxCell>
        <UserObject label="Create agent_run record" mermaidId="e:Backend-&gt;Database#11" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Create agent_run record" id="nThWUC4bMk5yji6sOE_n-67">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3119" />
              </Array>
              <mxPoint x="837" y="3119" as="sourcePoint" />
              <mxPoint x="1167" y="3119" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent_run" mermaidId="e:Database-&gt;Backend#11" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent_run" id="nThWUC4bMk5yji6sOE_n-68">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3163" />
              </Array>
              <mxPoint x="1167" y="3163" as="sourcePoint" />
              <mxPoint x="837" y="3163" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Insert agent_suggestions" mermaidId="e:Backend-&gt;Database#12" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Insert agent_suggestions" id="nThWUC4bMk5yji6sOE_n-69">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3207" />
              </Array>
              <mxPoint x="837" y="3207" as="sourcePoint" />
              <mxPoint x="1167" y="3207" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return suggestions" mermaidId="e:Database-&gt;Backend#12" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return suggestions" id="nThWUC4bMk5yji6sOE_n-70">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3251" />
              </Array>
              <mxPoint x="1167" y="3251" as="sourcePoint" />
              <mxPoint x="837" y="3251" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent_run_id and suggestions" mermaidId="e:Backend-&gt;Frontend#6" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent_run_id and suggestions" id="nThWUC4bMk5yji6sOE_n-71">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="3295" />
              </Array>
              <mxPoint x="837" y="3295" as="sourcePoint" />
              <mxPoint x="490" y="3295" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to AI Plan Review" mermaidId="e:Frontend-&gt;User#10" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to AI Plan Review" id="nThWUC4bMk5yji6sOE_n-72">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="3339" />
              </Array>
              <mxPoint x="490" y="3339" as="sourcePoint" />
              <mxPoint x="85" y="3339" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="View suggested subtasks" mermaidId="e:User-&gt;Frontend#14" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="View suggested subtasks" id="nThWUC4bMk5yji6sOE_n-73">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="3433" />
              </Array>
              <mxPoint x="85" y="3433" as="sourcePoint" />
              <mxPoint x="490" y="3433" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /agent-runs/{agent_run_id}" mermaidId="e:Frontend-&gt;Backend#7" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /agent-runs/{agent_run_id}" id="nThWUC4bMk5yji6sOE_n-74">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="3477" />
              </Array>
              <mxPoint x="490" y="3477" as="sourcePoint" />
              <mxPoint x="837" y="3477" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query agent run details" mermaidId="e:Backend-&gt;Database#13" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query agent run details" id="nThWUC4bMk5yji6sOE_n-75">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3521" />
              </Array>
              <mxPoint x="837" y="3521" as="sourcePoint" />
              <mxPoint x="1167" y="3521" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return run, suggestions, tool_calls" mermaidId="e:Database-&gt;Backend#13" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return run, suggestions, tool_calls" id="nThWUC4bMk5yji6sOE_n-76">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3565" />
              </Array>
              <mxPoint x="1167" y="3565" as="sourcePoint" />
              <mxPoint x="837" y="3565" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent run details" mermaidId="e:Backend-&gt;Frontend#7" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent run details" id="nThWUC4bMk5yji6sOE_n-77">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="3609" />
              </Array>
              <mxPoint x="837" y="3609" as="sourcePoint" />
              <mxPoint x="490" y="3609" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display suggestions with checkboxes" mermaidId="e:Frontend-&gt;User#11" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display suggestions with checkboxes" id="nThWUC4bMk5yji6sOE_n-78">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="3653" />
              </Array>
              <mxPoint x="490" y="3653" as="sourcePoint" />
              <mxPoint x="85" y="3653" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Select desired suggestions" mermaidId="e:User-&gt;Frontend#15" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Select desired suggestions" id="nThWUC4bMk5yji6sOE_n-79">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="3697" />
              </Array>
              <mxPoint x="85" y="3697" as="sourcePoint" />
              <mxPoint x="490" y="3697" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Accept Selected&quot;" mermaidId="e:User-&gt;Frontend#16" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Accept Selected&quot;" id="nThWUC4bMk5yji6sOE_n-80">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="3741" />
              </Array>
              <mxPoint x="85" y="3741" as="sourcePoint" />
              <mxPoint x="490" y="3741" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="POST /agent-runs/{agent_run_id}/accept" mermaidId="e:Frontend-&gt;Backend#8" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="POST /agent-runs/{agent_run_id}/accept" id="nThWUC4bMk5yji6sOE_n-81">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="3785" />
              </Array>
              <mxPoint x="490" y="3785" as="sourcePoint" />
              <mxPoint x="837" y="3785" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Verify ownership" mermaidId="e:Backend-&gt;Database#14" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Verify ownership" id="nThWUC4bMk5yji6sOE_n-82">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3829" />
              </Array>
              <mxPoint x="837" y="3829" as="sourcePoint" />
              <mxPoint x="1167" y="3829" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent run and project" mermaidId="e:Database-&gt;Backend#14" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent run and project" id="nThWUC4bMk5yji6sOE_n-83">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3873" />
              </Array>
              <mxPoint x="1167" y="3873" as="sourcePoint" />
              <mxPoint x="837" y="3873" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query selected suggestions" mermaidId="e:Backend-&gt;Database#15" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query selected suggestions" id="nThWUC4bMk5yji6sOE_n-84">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3917" />
              </Array>
              <mxPoint x="837" y="3917" as="sourcePoint" />
              <mxPoint x="1167" y="3917" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return suggestions" mermaidId="e:Database-&gt;Backend#15" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return suggestions" id="nThWUC4bMk5yji6sOE_n-85">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="3961" />
              </Array>
              <mxPoint x="1167" y="3961" as="sourcePoint" />
              <mxPoint x="837" y="3961" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Create subtasks from suggestions" mermaidId="e:Backend-&gt;Database#16" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Create subtasks from suggestions" id="nThWUC4bMk5yji6sOE_n-86">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4005" />
              </Array>
              <mxPoint x="837" y="4005" as="sourcePoint" />
              <mxPoint x="1167" y="4005" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return created subtasks" mermaidId="e:Database-&gt;Backend#16" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return created subtasks" id="nThWUC4bMk5yji6sOE_n-87">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4049" />
              </Array>
              <mxPoint x="1167" y="4049" as="sourcePoint" />
              <mxPoint x="837" y="4049" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Update suggestion status to &quot;accepted&quot;" mermaidId="e:Backend-&gt;Database#17" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Update suggestion status to &quot;accepted&quot;" id="nThWUC4bMk5yji6sOE_n-88">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4093" />
              </Array>
              <mxPoint x="837" y="4093" as="sourcePoint" />
              <mxPoint x="1167" y="4093" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Confirm update" mermaidId="e:Database-&gt;Backend#17" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Confirm update" id="nThWUC4bMk5yji6sOE_n-89">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4137" />
              </Array>
              <mxPoint x="1167" y="4137" as="sourcePoint" />
              <mxPoint x="837" y="4137" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return created subtasks" mermaidId="e:Backend-&gt;Frontend#8" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return created subtasks" id="nThWUC4bMk5yji6sOE_n-90">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4181" />
              </Array>
              <mxPoint x="837" y="4181" as="sourcePoint" />
              <mxPoint x="490" y="4181" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate back to Task Detail" mermaidId="e:Frontend-&gt;User#12" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate back to Task Detail" id="nThWUC4bMk5yji6sOE_n-91">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="4225" />
              </Array>
              <mxPoint x="490" y="4225" as="sourcePoint" />
              <mxPoint x="85" y="4225" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /tasks/{task_id}" mermaidId="e:Frontend-&gt;Backend#9" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /tasks/{task_id}" id="nThWUC4bMk5yji6sOE_n-92">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4269" />
              </Array>
              <mxPoint x="490" y="4269" as="sourcePoint" />
              <mxPoint x="837" y="4269" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query task with new subtasks" mermaidId="e:Backend-&gt;Database#18" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query task with new subtasks" id="nThWUC4bMk5yji6sOE_n-93">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4313" />
              </Array>
              <mxPoint x="837" y="4313" as="sourcePoint" />
              <mxPoint x="1167" y="4313" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task details" mermaidId="e:Database-&gt;Backend#18" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task details" id="nThWUC4bMk5yji6sOE_n-94">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4357" />
              </Array>
              <mxPoint x="1167" y="4357" as="sourcePoint" />
              <mxPoint x="837" y="4357" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return task with subtasks" mermaidId="e:Backend-&gt;Frontend#9" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return task with subtasks" id="nThWUC4bMk5yji6sOE_n-95">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4401" />
              </Array>
              <mxPoint x="837" y="4401" as="sourcePoint" />
              <mxPoint x="490" y="4401" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display task with accepted subtasks" mermaidId="e:Frontend-&gt;User#13" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display task with accepted subtasks" id="nThWUC4bMk5yji6sOE_n-96">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="4445" />
              </Array>
              <mxPoint x="490" y="4445" as="sourcePoint" />
              <mxPoint x="85" y="4445" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Agent Runs" mermaidId="e:User-&gt;Frontend#17" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Agent Runs" id="nThWUC4bMk5yji6sOE_n-97">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="4539" />
              </Array>
              <mxPoint x="85" y="4539" as="sourcePoint" />
              <mxPoint x="490" y="4539" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /agent-runs" mermaidId="e:Frontend-&gt;Backend#10" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /agent-runs" id="nThWUC4bMk5yji6sOE_n-98">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4583" />
              </Array>
              <mxPoint x="490" y="4583" as="sourcePoint" />
              <mxPoint x="837" y="4583" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query user&#39;s projects" mermaidId="e:Backend-&gt;Database#19" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query user&#39;s projects" id="nThWUC4bMk5yji6sOE_n-99">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4627" />
              </Array>
              <mxPoint x="837" y="4627" as="sourcePoint" />
              <mxPoint x="1167" y="4627" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return project IDs" mermaidId="e:Database-&gt;Backend#19" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return project IDs" id="nThWUC4bMk5yji6sOE_n-100">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4671" />
              </Array>
              <mxPoint x="1167" y="4671" as="sourcePoint" />
              <mxPoint x="837" y="4671" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query agent runs with filters" mermaidId="e:Backend-&gt;Database#20" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query agent runs with filters" id="nThWUC4bMk5yji6sOE_n-101">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4715" />
              </Array>
              <mxPoint x="837" y="4715" as="sourcePoint" />
              <mxPoint x="1167" y="4715" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent runs" mermaidId="e:Database-&gt;Backend#20" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent runs" id="nThWUC4bMk5yji6sOE_n-102">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4759" />
              </Array>
              <mxPoint x="1167" y="4759" as="sourcePoint" />
              <mxPoint x="837" y="4759" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent run history" mermaidId="e:Backend-&gt;Frontend#10" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent run history" id="nThWUC4bMk5yji6sOE_n-103">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4803" />
              </Array>
              <mxPoint x="837" y="4803" as="sourcePoint" />
              <mxPoint x="490" y="4803" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display agent run table" mermaidId="e:Frontend-&gt;User#14" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display agent run table" id="nThWUC4bMk5yji6sOE_n-104">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="4847" />
              </Array>
              <mxPoint x="490" y="4847" as="sourcePoint" />
              <mxPoint x="85" y="4847" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;View Run&quot;" mermaidId="e:User-&gt;Frontend#18" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;View Run&quot;" id="nThWUC4bMk5yji6sOE_n-105">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="4891" />
              </Array>
              <mxPoint x="85" y="4891" as="sourcePoint" />
              <mxPoint x="490" y="4891" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /agent-runs/{agent_run_id}" mermaidId="e:Frontend-&gt;Backend#11" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /agent-runs/{agent_run_id}" id="nThWUC4bMk5yji6sOE_n-106">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="4935" />
              </Array>
              <mxPoint x="490" y="4935" as="sourcePoint" />
              <mxPoint x="837" y="4935" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query agent run details" mermaidId="e:Backend-&gt;Database#21" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query agent run details" id="nThWUC4bMk5yji6sOE_n-107">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="4979" />
              </Array>
              <mxPoint x="837" y="4979" as="sourcePoint" />
              <mxPoint x="1167" y="4979" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return run, suggestions, tool_calls" mermaidId="e:Database-&gt;Backend#21" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return run, suggestions, tool_calls" id="nThWUC4bMk5yji6sOE_n-108">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="5023" />
              </Array>
              <mxPoint x="1167" y="5023" as="sourcePoint" />
              <mxPoint x="837" y="5023" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return agent run detail" mermaidId="e:Backend-&gt;Frontend#11" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return agent run detail" id="nThWUC4bMk5yji6sOE_n-109">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="5067" />
              </Array>
              <mxPoint x="837" y="5067" as="sourcePoint" />
              <mxPoint x="490" y="5067" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display run input, output, timing, tool calls" mermaidId="e:Frontend-&gt;User#15" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display run input, output, timing, tool calls" id="nThWUC4bMk5yji6sOE_n-110">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5111" />
              </Array>
              <mxPoint x="490" y="5111" as="sourcePoint" />
              <mxPoint x="85" y="5111" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Navigate to Integrations" mermaidId="e:User-&gt;Frontend#19" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Navigate to Integrations" id="nThWUC4bMk5yji6sOE_n-111">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5205" />
              </Array>
              <mxPoint x="85" y="5205" as="sourcePoint" />
              <mxPoint x="490" y="5205" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="GET /integrations" mermaidId="e:Frontend-&gt;Backend#12" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="GET /integrations" id="nThWUC4bMk5yji6sOE_n-112">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="5249" />
              </Array>
              <mxPoint x="490" y="5249" as="sourcePoint" />
              <mxPoint x="837" y="5249" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Query integrations" mermaidId="e:Backend-&gt;Database#22" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Query integrations" id="nThWUC4bMk5yji6sOE_n-113">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="5293" />
              </Array>
              <mxPoint x="837" y="5293" as="sourcePoint" />
              <mxPoint x="1167" y="5293" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return integrations" mermaidId="e:Database-&gt;Backend#22" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return integrations" id="nThWUC4bMk5yji6sOE_n-114">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="5337" />
              </Array>
              <mxPoint x="1167" y="5337" as="sourcePoint" />
              <mxPoint x="837" y="5337" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return integrations" mermaidId="e:Backend-&gt;Frontend#12" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return integrations" id="nThWUC4bMk5yji6sOE_n-115">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="5381" />
              </Array>
              <mxPoint x="837" y="5381" as="sourcePoint" />
              <mxPoint x="490" y="5381" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display connections table" mermaidId="e:Frontend-&gt;User#16" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display connections table" id="nThWUC4bMk5yji6sOE_n-116">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5425" />
              </Array>
              <mxPoint x="490" y="5425" as="sourcePoint" />
              <mxPoint x="85" y="5425" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Click &quot;Connect GitHub MCP&quot;" mermaidId="e:User-&gt;Frontend#20" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Click &quot;Connect GitHub MCP&quot;" id="nThWUC4bMk5yji6sOE_n-117">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5469" />
              </Array>
              <mxPoint x="85" y="5469" as="sourcePoint" />
              <mxPoint x="490" y="5469" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Provide configuration reference" mermaidId="e:User-&gt;Frontend#21" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Provide configuration reference" id="nThWUC4bMk5yji6sOE_n-118">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-2" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5513" />
              </Array>
              <mxPoint x="85" y="5513" as="sourcePoint" />
              <mxPoint x="490" y="5513" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="POST /integrations/github-mcp/connect" mermaidId="e:Frontend-&gt;Backend#13" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="POST /integrations/github-mcp/connect" id="nThWUC4bMk5yji6sOE_n-119">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="5557" />
              </Array>
              <mxPoint x="490" y="5557" as="sourcePoint" />
              <mxPoint x="837" y="5557" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="" mermaidId="e:Backend-&gt;Backend#1" mermaidBaseStyle="edgeStyle=none;curved=1;endArrow=block;endSize=9;verticalAlign=bottom;align=center;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="" id="nThWUC4bMk5yji6sOE_n-120">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="edgeStyle=none;curved=1;endArrow=block;endSize=9;verticalAlign=bottom;align=center;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="872" y="5631" />
                <mxPoint x="876" y="5643" />
                <mxPoint x="872" y="5655" />
              </Array>
              <mxPoint x="837" y="5631" as="sourcePoint" />
              <mxPoint x="837" y="5655" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <mxCell id="nThWUC4bMk5yji6sOE_n-121" parent="oOSgu5qEeW-CKJ_P9lIY-0" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;fontColor=light-dark(#333333,#cccccc);" value="Validate MCP configuration" vertex="1">
          <mxGeometry height="18" width="200" x="737" y="5607" as="geometry" />
        </mxCell>
        <UserObject label="Insert integration record" mermaidId="e:Backend-&gt;Database#23" mermaidBaseStyle="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Insert integration record" id="nThWUC4bMk5yji6sOE_n-122">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-5">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="5705" />
              </Array>
              <mxPoint x="837" y="5705" as="sourcePoint" />
              <mxPoint x="1167" y="5705" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return integration" mermaidId="e:Database-&gt;Backend#23" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return integration" id="nThWUC4bMk5yji6sOE_n-123">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-5" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-4">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="1002" y="5749" />
              </Array>
              <mxPoint x="1167" y="5749" as="sourcePoint" />
              <mxPoint x="837" y="5749" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Return connection status" mermaidId="e:Backend-&gt;Frontend#13" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Return connection status" id="nThWUC4bMk5yji6sOE_n-124">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-4" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-3">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="664" y="5793" />
              </Array>
              <mxPoint x="837" y="5793" as="sourcePoint" />
              <mxPoint x="490" y="5793" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="Display updated integrations" mermaidId="e:Frontend-&gt;User#17" mermaidBaseStyle="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" mermaidBaseValue="Display updated integrations" id="nThWUC4bMk5yji6sOE_n-125">
          <mxCell edge="1" parent="oOSgu5qEeW-CKJ_P9lIY-0" source="nThWUC4bMk5yji6sOE_n-3" style="dashed=1;fixDash=1;dashPattern=3 3;endArrow=block;endSize=9;verticalAlign=bottom;edgeStyle=elbowEdgeStyle;elbow=vertical;curved=0;rounded=0;fontSize=16;labelBackgroundColor=none;strokeWidth=1.5;strokeColor=light-dark(#333333,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;" target="nThWUC4bMk5yji6sOE_n-2">
            <mxGeometry relative="1" as="geometry">
              <Array as="points">
                <mxPoint x="288" y="5837" />
              </Array>
              <mxPoint x="490" y="5837" as="sourcePoint" />
              <mxPoint x="85" y="5837" as="targetPoint" />
            </mxGeometry>
          </mxCell>
        </UserObject>
        <UserObject label="1. Open Projects" mermaidId="n:note0" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="1. Open Projects" id="nThWUC4bMk5yji6sOE_n-126">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="85" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="2. Create Project" mermaidId="n:note1" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="2. Create Project" id="nThWUC4bMk5yji6sOE_n-127">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="487" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="3. Add Tasks" mermaidId="n:note2" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="3. Add Tasks" id="nThWUC4bMk5yji6sOE_n-128">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="933" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="4. Update Status/Priority" mermaidId="n:note3" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="4. Update Status/Priority" id="nThWUC4bMk5yji6sOE_n-129">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="1467" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="5. Open Task" mermaidId="n:note4" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="5. Open Task" id="nThWUC4bMk5yji6sOE_n-130">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="2001" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="6. Ask Planning Agent for Subtasks" mermaidId="n:note5" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="6. Ask Planning Agent for Subtasks" id="nThWUC4bMk5yji6sOE_n-131">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="2667" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="7. Review and Accept Selected Suggestions" mermaidId="n:note6" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="7. Review and Accept Selected Suggestions" id="nThWUC4bMk5yji6sOE_n-132">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="3349" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="8. Inspect Agent Runs/Tool Calls" mermaidId="n:note7" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="8. Inspect Agent Runs/Tool Calls" id="nThWUC4bMk5yji6sOE_n-133">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="4455" as="geometry" />
          </mxCell>
        </UserObject>
        <UserObject label="9. Connect GitHub MCP Integration (Later)" mermaidId="n:note8" mermaidBaseStyle="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" mermaidBaseValue="9. Connect GitHub MCP Integration (Later)" id="nThWUC4bMk5yji6sOE_n-134">
          <mxCell parent="oOSgu5qEeW-CKJ_P9lIY-0" style="html=1;fillColor=light-dark(#fff5ad,#2a2a2a);strokeColor=light-dark(#aaaa33,#cccccc);fontColor=light-dark(#333333,#cccccc);fontFamily=Trebuchet MS,Verdana,Arial,sans-serif;fontSize=16;" vertex="1">
            <mxGeometry height="40" width="1122" x="65" y="5121" as="geometry" />
          </mxCell>
        </UserObject>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

```