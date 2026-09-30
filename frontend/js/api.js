// API Client for ProjectFlow AI

const API_BASE_URL = 'http://localhost:8000';

class APIClient {
  constructor(baseURL) {
    this.baseURL = baseURL;
  }

  getAuthHeaders() {
    const token = localStorage.getItem('access_token');
    if (token) {
      return {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      };
    }
    return {
      'Content-Type': 'application/json'
    };
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      ...options,
      headers: {
        ...this.getAuthHeaders(),
        ...options.headers
      }
    };

    try {
      const response = await fetch(url, config);
      
      if (response.status === 401) {
        // Unauthorized - clear token and redirect to login
        localStorage.removeItem('access_token');
        window.location.href = '/frontend/index.html';
        throw new Error('Unauthorized');
      }

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'An error occurred');
      }

      return data;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }

  // Auth endpoints
  async register(name, email, password) {
    return this.request('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ name, email, password })
    });
  }

  async login(email, password) {
    return this.request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password })
    });
  }

  // Projects endpoints
  async getProjects() {
    return this.request('/projects');
  }

  async getProject(projectId) {
    return this.request(`/projects/${projectId}`);
  }

  async createProject(data) {
    return this.request('/projects', {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  async updateProject(projectId, data) {
    return this.request(`/projects/${projectId}`, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  // Tasks endpoints
  async getTasks(projectId, filters = {}) {
    const params = new URLSearchParams(filters);
    return this.request(`/projects/${projectId}/tasks?${params}`);
  }

  async getTask(taskId) {
    return this.request(`/tasks/${taskId}`);
  }

  async createTask(projectId, data) {
    return this.request(`/projects/${projectId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  async updateTask(taskId, data) {
    return this.request(`/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  async deleteTask(taskId) {
    return this.request(`/tasks/${taskId}`, {
      method: 'DELETE'
    });
  }

  // AI Planning endpoints
  async planTask(taskId, taskContext = '') {
    return this.request(`/tasks/${taskId}/plan`, {
      method: 'POST',
      body: JSON.stringify({ task_context: taskContext })
    });
  }

  // Agent Runs endpoints
  async getAgentRuns(filters = {}) {
    const params = new URLSearchParams(filters);
    return this.request(`/agent-runs?${params}`);
  }

  async getAgentRun(agentRunId) {
    return this.request(`/agent-runs/${agentRunId}`);
  }

  async acceptSuggestions(agentRunId, suggestionIds) {
    return this.request(`/agent-runs/${agentRunId}/accept`, {
      method: 'POST',
      body: JSON.stringify({ selected_suggestion_ids: suggestionIds })
    });
  }

  async rejectPlan(agentRunId) {
    return this.request(`/agent-runs/${agentRunId}/reject`, {
      method: 'POST'
    });
  }

  // Integrations endpoints
  async getIntegrations() {
    return this.request('/integrations');
  }

  async connectGitHubMCP(configReference) {
    return this.request('/integrations/github-mcp/connect', {
      method: 'POST',
      body: JSON.stringify({ configuration_reference: configReference })
    });
  }

  async testIntegration(integrationId) {
    return this.request(`/integrations/${integrationId}/test`, {
      method: 'POST'
    });
  }

  async disconnectIntegration(integrationId) {
    return this.request(`/integrations/${integrationId}`, {
      method: 'DELETE'
    });
  }
}

const api = new APIClient(API_BASE_URL);
