// Navigation utilities

function initializeNavigation() {
  const currentPage = window.location.pathname.split('/').pop();
  const navLinks = document.querySelectorAll('.sidebar-nav a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.includes(currentPage)) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

function setupLogout() {
  const logoutBtn = document.getElementById('logout-btn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault();
      logout();
    });
  }
}

function displayUserInfo() {
  const user = getCurrentUser();
  const userNameEl = document.getElementById('user-name');
  if (userNameEl && user) {
    userNameEl.textContent = user.name;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initializeNavigation();
  setupLogout();
  displayUserInfo();
});
