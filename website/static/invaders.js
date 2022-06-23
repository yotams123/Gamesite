
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
    this.maxBullets = 2;
}

Player.prototype.draw = function(){
    this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y, this.width, this.height);
}

Player.prototype.spawnBullet = function() {
    this.bullets.push(new Bullet(this, this.canvas));
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
        x: player.position.x + player.width/2,
        y: player.position.y
    };

    this.speed = 7;

    this.color = "#ff0000";

    this.width = 2;
    this.length = 10;
}

Bullet.prototype.move = function(){
    this.canvas.drawer.clearRect(this.position.x - 1, this.position.y - 1, this.width + 2, this.length + 2);
    this.position.y -= this.speed; 
    this.canvas.drawer.fillStyle = this.color;
    this.canvas.drawer.fillRect(this.position.x, this.position.y, this.width, this.length);
    if (this.position.y <= 0){
        this.destroy();
    }
}

Bullet.prototype.destroy = function(){
    this.canvas.drawer.clearRect(this.position.x - 1, this.position.y, this.width + 2, this.length+ 2)
    const index = this.player.bullets.indexOf(this);
    this.player.bullets.splice(index, 1);
}

function Invader(canvas, position){
    const image = new Image();
    image.src = "../static/img/invader.png";
    this.image = image;

    this.canvas = canvas;

    this.width = 40;
    this.height = 40;

    this.position = {
        x: position.x,
        y: position.y
    };
}

Invader.prototype.clear = function(){
    this.canvas.drawer.clearRect(this.position.x - 1, this.position.y - 1, this.width + 2, this.height + 2)
}

Invader.prototype.draw = function(){
    this.canvas.drawer.drawImage(this.image, this.position.x, this.position.y, this.width, this.height);
}

function InvaderGrid(){
    this.position= {
        x: 10,
        y: 0
    };

    this.speed = {
        x: 1,
        y: 0
    };

    this.cols = Math.floor(Math.random() * 7 + 3); //number of columns
    this.rows = Math.floor(Math.random() * 4 + 1); //number of rows

    this.invaders = [];
    const o = new Invader(canvas, {x: 0, y: 0});
    for (let i = 0; i<this.rows; i++){
        for (let j = 0; j<this.cols; j++){
            this.invaders.push(new Invader(canvas, {x: this.position.x + o.width * j, y: this.position.y + o.height * i}));
        }
    }
}

InvaderGrid.prototype.move = function(){
    this.invaders.forEach(i => i.clear())  
    
    const invader = new Invader(canvas, {x: 0, y: 0});
    
    if (this.position.x <= 0 || this.position.x >= invader.canvas.width - invader.width * this.cols){
        this.speed.x *= -1;
        this.speed.y = invader.height;
    }
    
    this.position.x += this.speed.x;
    this.position.y += this.speed.y;

    const g = this;
    this.invaders.forEach(i => {i.position.x += g.speed.x;
        i.position.y += g.speed.y;});
    
    this.speed.y = 0;
    
    this.invaders.forEach(i => i.draw());
}

const canvas = new Canvas();
const player = new Player(canvas);
const grids = [];

let interval = Math.floor((Math.random() * 500) + 1000)
let frames = 0;

function run(){
    requestAnimationFrame(run);
    player.draw();
    player.bullets.forEach(bullet => bullet.move());
    
    if (frames %  interval === 0){
        grids.push(new InvaderGrid());
        interval = Math.floor((Math.random() * 500) + 1000);

        frames = 0;
    }

    for (let g of grids){
        g.move();
        g.invaders.forEach((i, ind) => {
            for (let bullet of player.bullets){
                console.log(i.length);
                if ( i.position.y < bullet.position.y && bullet.position.y < i.position.y + i.height 
                    && i.position.x < bullet.position.x && bullet.position.x < i.position.x + i.width){
                        i.clear();
                        g.invaders.splice(ind, 1);
                        bullet.destroy();
                    }
            }
        })
    }

    frames++;
}

run();
document.addEventListener('keydown', function(e){player.control(e)})