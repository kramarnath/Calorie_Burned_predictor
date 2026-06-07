document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Stop standard form submission

        const inputs = Array.from(document.querySelectorAll('input'));
        const currentIndex = inputs.indexOf(document.activeElement);

        if (currentIndex > -1 && currentIndex + 1 < inputs.length) {
            // Move focus to the next input field
            inputs[currentIndex + 1].focus();
        } else if (currentIndex === inputs.length - 1) {
            // last button
            const predictBtn = document.querySelector('.predict-btn');
            if (predictBtn) {
                predictBtn.click();
            }
        }
    }
});
