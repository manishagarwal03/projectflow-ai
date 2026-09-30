// Authentication utilities

function saveAuthToken(token, user) {
  localStorage.setItem('access_token', token);
  localStorage.setItem('user', JSON.stringify(user));
}

function getAuthToken() {
  return localStorage.getItem('access_token');
}

function getCurrentUser() {
  const userStr = localStorage.getItem('user');
  return userStr ? JSON.parse(userStr) : null;
}

function isAuthenticated() {
  return !!getAuthToken();
}

function logout() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('user');
  window.location.href = '/frontend/index.html';
}

function requireAuth() {
  if (!isAuthenticated()) {
    window.location.href = '/frontend/index.html';
  }
}
