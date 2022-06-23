
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

    this.bullets = [];
    this.maxBullets = 10;
}

Player.prototype.draw = function(){
    this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y, this.width, this.height);
}

Player.prototype.spawnBullet = function() {
    this.bullets.push(new Bullet(this, this.canvas));
    console.log("here");
};

Player.prototype.control= function(e){
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
        case 32:
            if (this.bullets.length < this.maxBullets){
                this.spawnBullet();
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

function Bullet(player, canvas){

    this.player = player;
    this.canvas = canvas;

    this.position = {
        x: player.position.x,
        y: player.position.y
    };

    this.speed = 7;

    this.color = "#ff0000";

    this.width = 2;
    this.height = 10;
}

Bullet.prototype.move = function(){
    this.canvas.drawer.clearRect(this.position.x - 1, this.position.y - 1, this.width + 2, this.height + 2);
    this.position.y -= this.speed; 
    this.canvas.drawer.fillStyle = this.color;
    this.canvas.drawer.fillRect(this.position.x, this.position.y, this.width, this.height);
}

const canvas = new Canvas();
const player = new Player(canvas);

function run(){
    requestAnimationFrame(run);
    player.draw();
    for (let bullet of player.bullets){
        bullet.move();
    }
}

run();
document.addEventListener('keydown', function(e){player.control(e)})