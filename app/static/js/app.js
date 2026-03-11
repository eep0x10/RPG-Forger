// Feiticeiros & Maldições – JS utilitário

// Previne double-submit em forms
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function () {
      const btn = this.querySelector('button[type="submit"]');
      if (btn && !btn.disabled) {
        btn.disabled = true;
        btn.textContent = 'Aguarde...';
      }
    });
  });

  // Auto-resize textareas
  document.querySelectorAll('textarea').forEach(ta => {
    ta.addEventListener('input', function () {
      this.style.height = 'auto';
      this.style.height = this.scrollHeight + 'px';
    });
  });
});
