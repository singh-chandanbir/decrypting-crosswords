var socket = io();


socket.on('connect', function() {
});

socket.on('gameData', function(message) {

    blocked_cell_list = message['blocked_cell_list'];
    grid  = message['grid'];
    order = message['order'];

    for (var i = 0; i < blocked_cell_list.length; i++) {
        document.getElementById(blocked_cell_list[i]).disabled = true;
        document.getElementById(blocked_cell_list[i]).closest('td').style.backgroundColor = "black";
      }


});
socket.on('test', function(message) {
   console.log(message);
});


function start_timer() {
    var sec = 1;
    var min = 0;
    var timer = setInterval(function () {
        if (sec < 10) {
            dis_sec = '0' + sec;
        } else { dis_sec = sec; }

        if (min < 10) {
            dis_min = '0' + min;
        } else { dis_min = min; }

        document.getElementById('timer').innerHTML = dis_min + ':' + dis_sec;
        sec++;
        if (sec == 60) {
            sec = 0;
            min++;
        }
    }, 1000);
    
    // Return the timer so it can be cleared later
    return timer;
}

// Global variable to hold the timer
var timer;

function stop_timer() {
    clearInterval(timer); // Clear the interval timer
}



function startgame() {
    timer = start_timer(); // Start the timer and store the timer ID
    document.getElementById("start-btn-wrapper").style.display = "none";
    document.getElementById("btn-wrapper").style.display = "flex";
    
    let startTime = new Date().getTime(); // Get the current time in milliseconds

    socket.emit('time', {'startTime': startTime });
}

function endgame() {
    stop_timer(); // Stop the timer
    let endTime = new Date().getTime(); // Get the current time in milliseconds
    socket.emit('time', {'endTime': endTime });
}

function clearAll() {
    let inputboxs = document.getElementsByClassName("inputbox");
    for (const iterator of inputboxs) {
        iterator.value = "";
    }
}



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var bot = document.getElementById("think")
async function delayedLoop() {
    bot.style.display = "block";
    console.log(bot)
    for (const key in order) {
        let x = order[key][0];
        let y = order[key][1];
        let prefix = "input";
        let id = prefix + x + "-" + y;
        if (grid[x][y] != "") {
            var delay = 50;
            await sleep(delay);
            document.getElementById(id).value = grid[x][y];
        };
    };
    bot.style.display = "none";

}

