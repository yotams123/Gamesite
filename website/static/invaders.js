
function Player(canvas){
    this.height = 50;
    this.width = 50;

    this.canvas = canvas;

    this.position = {
        x: (this.canvas.width-this.width)/2,
        y: (this.canvas.height - this.height) * 0.9
    };

    this.speed = {
        x: 3,
        y: 3
    };

    const image = new Image();
    image.src = "./static/img/spaceship.png";
    this.image = image;
}

Player.prototype.draw = function(){
    this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y, this.width, this.height);
}

function Canvas(){
    const canvas = document.querySelector("canvas");
    
    this.canvas = canvas;
    this.drawer = canvas.getContext("2d");

    this.width = canvas.width = innerWidth * 0.7;
    this.height = canvas.height = innerHeight * 0.8;
}

const canvas = new Canvas();
const player = new Player(canvas);

function run(){
    requestAnimationFrame(run);
    player.draw();
}

run();