document.addEventListener('DOMContentLoaded', function() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Preview image URL in product form
    const imageUrlInput = document.getElementById('image_url');
    if (imageUrlInput) {
        imageUrlInput.addEventListener('change', function() {
            const url = this.value;
            if (url) {
                const img = new Image();
                img.onload = function() {
                    imageUrlInput.classList.remove('is-invalid');
                    imageUrlInput.classList.add('is-valid');
                };
                img.onerror = function() {
                    imageUrlInput.classList.remove('is-valid');
                    imageUrlInput.classList.add('is-invalid');
                };
                img.src = url;
            }
        });
    }
});
