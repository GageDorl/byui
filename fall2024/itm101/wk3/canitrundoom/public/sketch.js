let ship;
let asteroids = [];
let lasers = [];

function setup() {
  createCanvas(1400, 750);
  ship = new Ship();
  for (let i = 0; i < 5; i++) {
    asteroids.push(new Asteroid());
  }
}

function draw() {
  background(0);

  // Display and update ship
  ship.update();
  ship.render();
  ship.turn();
  ship.edges();

  // Display and update lasers
  for (let i = lasers.length - 1; i >= 0; i--) {
    lasers[i].update();
    lasers[i].render();
    if (lasers[i].offscreen()) {
      lasers.splice(i, 1);
    } else {
      for (let j = asteroids.length - 1; j >= 0; j--) {
        if (lasers[i].hits(asteroids[j])) {
          let newAsteroids = asteroids[j].breakup();
          asteroids = asteroids.concat(newAsteroids);
          asteroids.splice(j, 1);
          lasers.splice(i, 1);
          break;
        }
      }
    }
  }

  // Display and update asteroids
  for (let i = 0; i < asteroids.length; i++) {
    asteroids[i].render();
    asteroids[i].update();
    asteroids[i].edges();
  }
}

function keyPressed() {
  if (key === ' ') {
    lasers.push(new Laser(ship.pos, ship.heading));
  }
  if (keyCode === RIGHT_ARROW) {
    ship.setRotation(0.1);
  } else if (keyCode === LEFT_ARROW) {
    ship.setRotation(-0.1);
  } else if (keyCode === UP_ARROW) {
    ship.setBoosting(true);
  }
}

function keyReleased() {
    if (key === ' ') {
        return;
      }
      if (keyCode === RIGHT_ARROW) {
        ship.setRotation(0);
      } else if (keyCode === LEFT_ARROW) {
        ship.setRotation(0);
      } else if (keyCode === UP_ARROW) {
        ship.setBoosting(false);
      }
}

// Ship class
class Ship {
    constructor() {
      this.pos = createVector(width / 2, height / 2);  // Ship's position (centered on the canvas)
      this.r = 20;                                    // Ship's size (radius of the triangle)
      this.heading = 0;                               // Ship's rotation angle
      this.rotation = 0;                              // Rotation speed
      this.vel = createVector(0, 0);                  // Ship's velocity
      this.isBoosting = false;                        // Ship boosting state
    }
  
    // Update ship position and handle boosting
    update() {
      if (this.isBoosting) {
        this.boost();
      }
      this.pos.add(this.vel);  // Add velocity to position
      this.vel.mult(0.99);     // Apply friction to slow down over time
    }
  
    // Boost the ship's speed in the direction it's facing
    boost() {
      let force = p5.Vector.fromAngle(this.heading);  // Create a force vector in the direction of the ship's heading
      force.mult(0.1);                               // Scale the force to control boost speed
      this.vel.add(force);                            // Apply the force to the ship's velocity
    }
  
    // Render the ship as a triangle
    render() {
      push();                                        // Start a new drawing state
      translate(this.pos.x, this.pos.y);             // Move the origin to the ship's position
      rotate(this.heading+Math.PI/2);                          // Rotate the ship based on its heading
      fill(0);                                       // Fill color for the ship
      stroke(255);                                   // Outline color for the ship
      triangle(-this.r, this.r, this.r, this.r, 0, -this.r);  // Draw the triangle
      pop();                                         // Restore the previous drawing state
    }
  
    // Set ship's rotation angle (controls ship turning)
    setRotation(a) {
      this.rotation = a;
    }
  
    // Turn the ship by adding the rotation speed to the heading
    turn() {
      this.heading += this.rotation;
    }
  
    // Enable or disable boosting
    setBoosting(b) {
      this.isBoosting = b;
    }
  
    // Ensure the ship wraps around the screen edges
    edges() {
      if (this.pos.x > width + this.r) {
        this.pos.x = -this.r;
      } else if (this.pos.x < -this.r) {
        this.pos.x = width + this.r;
      }
      if (this.pos.y > height + this.r) {
        this.pos.y = -this.r;
      } else if (this.pos.y < -this.r) {
        this.pos.y = height + this.r;
      }
    }
  }
  

// Asteroid class
class Asteroid {
  constructor(pos, r) {
    if (pos) {
      this.pos = pos.copy();
    } else {
      this.pos = createVector(random(width), random(height));
    }
    if (r) {
      this.r = r * 0.5;
    } else {
      this.r = random(30, 50);
    }
    this.vel = p5.Vector.random2D();
    this.total = floor(random(5, 15));
    this.offset = [];
    for (let i = 0; i < this.total; i++) {
      this.offset[i] = random(-this.r * 0.5, this.r * 0.5);
    }
  }

  update() {
    this.pos.add(this.vel);
  }

  render() {
    push();
    stroke(255);
    noFill();
    translate(this.pos.x, this.pos.y);
    beginShape();
    for (let i = 0; i < this.total; i++) {
      let angle = map(i, 0, this.total, 0, TWO_PI);
      let r = this.r + this.offset[i];
      let x = r * cos(angle);
      let y = r * sin(angle);
      vertex(x, y);
    }
    endShape(CLOSE);
    pop();
  }

  edges() {
    if (this.pos.x > width + this.r) {
      this.pos.x = -this.r;
    } else if (this.pos.x < -this.r) {
      this.pos.x = width + this.r;
    }
    if (this.pos.y > height + this.r) {
      this.pos.y = -this.r;
    } else if (this.pos.y < -this.r) {
      this.pos.y = height + this.r;
    }
  }

  breakup() {
    let newA = [];
    newA[0] = new Asteroid(this.pos, this.r);
    newA[1] = new Asteroid(this.pos, this.r);
    return newA;
  }
}

// Laser class
class Laser {
    constructor(spos, angle) {
      // The laser is spawned from the ship's tip, so calculate that point.
      this.pos = createVector(spos.x + cos(angle) * 20, spos.y + sin(angle) * 20);  // Adjust the starting point to the tip of the ship
      this.vel = p5.Vector.fromAngle(angle);  // Laser direction
      this.vel.mult(10);  // Laser speed
    }
  
    update() {
      this.pos.add(this.vel);  // Move the laser
    }
  
    render() {
      push();
      stroke(255);
      strokeWeight(4);
      point(this.pos.x, this.pos.y);  // Render the laser as a point
      pop();
    }
  
    offscreen() {
      // Check if the laser goes off-screen
      if (this.pos.x > width || this.pos.x < 0 || this.pos.y > height || this.pos.y < 0) {
        return true;
      }
      return false;
    }
  
    hits(asteroid) {
      // Check for collision with an asteroid
      let d = dist(this.pos.x, this.pos.y, asteroid.pos.x, asteroid.pos.y);
      if (d < asteroid.r) {
        return true;
      }
      return false;
    }
  }
  