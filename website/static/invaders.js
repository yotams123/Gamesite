
function Player(canvas){
    this.canvas = canvas;

    this.height = this.canvas.height/9;
    this.width = this.canvas.width/18;

    this.position = {
        x: (this.canvas.width-this.width)/2,
        y: (this.canvas.height - this.height) * 0.9
    };

    this.speed = {
        x: 5,
        y: 3
    };

    const image = new Image();
    image.src = "./static/img/spaceship.png";
    this.image = image;
}

Player.prototype.draw = function(){
    this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y, this.width, this.height);
}

Player.prototype.move= function(e){
    this.canvas.drawer.clearRect(this.position.x, this.position.y, this.width, this.height);
    keyId = e.charCode? e.charCode: e.which? e.which: e.keycode;
    switch (keyId){
        case 37: //left
            if (this.position.x - this.speed.x >= 0)    
            {
                this.position.x -= this.speed.x;
            }
            break;
        case 38: //up
            if (this.position.y - this.speed.y >= 0){
                    this.position.y -= this.speed.y;
            }
            break;
        case 39: //right
            if (this.position.x + this.speed.x + this.width <= this.canvas.width){
                this.position.x += this.speed.x;
            }
            break;
        case 40: //down
            if (this.position.y + this.speed.y + this.height <= this.canvas.height)    
            {
                this.position.y += this.speed.y;
            }
            break;
    }
}

function Canvas(){
    const canvas = document.querySelector("canvas");
    
    this.canvas = canvas;
    this.drawer = canvas.getContext("2d");

    this.width = canvas.width = innerWidth * 0.7;
    this.height = canvas.height = innerHeight * 0.7;
}

const canvas = new Canvas();
const player = new Player(canvas);

function run(){
    requestAnimationFrame(run);
    player.draw();
}

run();
document.addEventListener('keydown', function(e){player.move(e)})