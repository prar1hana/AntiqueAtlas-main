document.addEventListener("DOMContentLoaded", function() {
    const track = document.getElementById("image-track");

    let isDragging = false;
    let startX, startY, scrollLeft, percentageBeforeDrag;

    window.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.pageX;
        startY = e.pageY;
        scrollLeft = track.scrollLeft;
        percentageBeforeDrag = parseFloat(track.dataset.percentage) || 0;
    });

    window.addEventListener('mouseup', () => {
        isDragging = false;
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;

        const deltaX = startX - e.pageX;
        const deltaY = startY - e.pageY;
        const maxDelta = window.innerWidth / 4;

        // Ensure the movement is only to the left
        const percentageChange = Math.min(0, deltaX / maxDelta * 100);
        const nextPercentage = percentageBeforeDrag + percentageChange;

        track.dataset.percentage = nextPercentage;
        track.style.transition = "none";
        track.style.transform = `translate(${nextPercentage}%, 0)`;

        const images = track.getElementsByClassName("image");
        for (const image of images) {
            image.style.transition = "none";
            image.style.objectPosition = `${nextPercentage + 100}% center`;
        }
    });

    track.addEventListener('mouseenter', () => {
        track.style.transition = "transform 0.5s ease-in-out";
        track.style.transform = "translate(0%, 0%)";
    });

    track.addEventListener('mouseleave', () => {
        track.style.transition = "transform 0.5s ease-in-out";
        track.style.transform = "translate(0%, 0%)";
    });
});
