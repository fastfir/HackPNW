window.addEventListener('load', function() {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 800;
    canvas.height = 800;

    ctx.fillStyle = "#808080";
    ctx.fillRect(100, 50, 150, 150);
    ctx.fillStyle = "#808080";
    ctx.fillRect(130, 300, 150, 150);

});