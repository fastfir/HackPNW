window.addEventListener('load', function() {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 800;
    canvas.height = 800;
    ctx.fillStyle = "#34dbeb";
    ctx.fillRect(400, 50, 400, 150);

    ctx.fillStyle = "black";
    ctx.font = "48px sans-serif";
    ctx.fillText("Protesting Game", 420, 140);

    const img = new Image();
    img.addEventListener(
  	"load",
  () => {
    // execute drawImage statements here
  },
  false
);
img.src = "menu button.svg"; // Set source path

});