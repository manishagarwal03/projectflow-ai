// Utility functions

function formatDate(isoString) {
  if (!isoString) return 'N/A';
  const date = new Date(isoString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  });
}

function formatDateTime(isoString) {
  if (!isoString) return 'N/A';
  const date = new Date(isoString);
  return date.toLocaleString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

function showAlert(message, type = 'info') {
  const alertDiv = document.createElement('div');
  alertDiv.className = `alert alert-${type}`;
  alertDiv.textContent = message;
  
  const container = document.querySelector('.main-content') || document.body;
  container.insertBefore(alertDiv, container.firstChild);
  
  setTimeout(() => {
    alertDiv.remove();
  }, 5000);
}

function showError(message) {
  showAlert(message, 'error');
}

function showSuccess(message) {
  showAlert(message, 'success');
}

function showInfo(message) {
  showAlert(message, 'info');
}

function showLoading(element) {
  element.innerHTML = '<div class="spinner"></div>';
}

function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

function setQueryParam(param, value) {
  const url = new URL(window.location);
  url.searchParams.set(param, value);
  window.history.pushState({}, '', url);
}

function getStatusBadgeClass(status) {
  const statusMap = {
    'active': 'badge-success',
    'paused': 'badge-warning',
    'completed': 'badge-info',
    'todo': 'badge-secondary',
    'in_progress': 'badge-warning',
    'done': 'badge-success',
    'running': 'badge-warning',
    'failed': 'badge-error',
    'rejected': 'badge-error',
    'pending': 'badge-secondary',
    'accepted': 'badge-success',
    'connected': 'badge-success',
    'disconnected': 'badge-secondary',
    'error': 'badge-error'
  };
  return statusMap[status] || 'badge-secondary';
}

function getPriorityBadgeClass(priority) {
  const priorityMap = {
    'low': 'badge-secondary',
    'medium': 'badge-info',
    'high': 'badge-warning',
    'critical': 'badge-error'
  };
  return priorityMap[priority] || 'badge-secondary';
}

function formatStatusLabel(status) {
  return status.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

function toggleMobileMenu() {
  const sidebar = document.querySelector('.sidebar');
  if (sidebar) {
    sidebar.classList.toggle('mobile-visible');
  }
}
