function attachGradientEvents() {
    const gradientElement = document.getElementById('gradient');
    const resultElement = document.getElementById('result');

    gradientElement.addEventListener('mousemove', (event) => {
        const percent = Math.floor(event.offsetX / event.target.clientWidth * 100);
        resultElement.textContent = `${percent}%`;
    });
}