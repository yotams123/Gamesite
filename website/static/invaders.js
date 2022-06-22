
function Player(canvas){
    this.position = {
        x: 100,
        y: 100
    };

    this.height = 50;
    this.width = 50;

    this.speed = {
        x: 3,
        y: 3
    };

    const image = new Image();
    image.src = "./static/img/spaceship.png";
    this.image = image;

    this.canvas = canvas;

    this.draw = function(){
        this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y);
    }
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