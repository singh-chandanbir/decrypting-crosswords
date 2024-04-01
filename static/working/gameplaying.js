// Used in: templates/gameplay.html

// let inputId_clueId = {};
var socket = io();

let previosly_target_input = {};

socket.on('connect', function () {
});


// FEF9C3


socket.on('gameData', function (message) {

    grid = message['grid'];
    order = message['order'];
    inputId_clueId = message['inputId_clueId'];
    // console.log("inputId_clueId", inputId_clueId)

    for (var i = 0; i < blocked_cell_list.length; i++) {
        document.getElementById(blocked_cell_list[i]).disabled = true;
        document.getElementById(blocked_cell_list[i]).closest('td').style.backgroundColor = "black";
    }

    function handleClick(event) {

        // console.log("previosly_target_input", previosly_target_input)

        for (var i = 0; i < previosly_target_input.length; i++) {
            document.getElementById(previosly_target_input[i]).style.backgroundColor = "transparent";
        }

        let selected_clue = event.target.className;
        // console.log("selected_clue", selected_clue)

        for (const key in inputId_clueId) {

            // console.log("key", key)

            if (key === selected_clue) {
                previosly_target_input = inputId_clueId[key];
                // console.log(inputId_clueId[key])
                document.getElementById(inputId_clueId[key][0]).focus();
                for (var i = 0; i < inputId_clueId[key].length; i++) {
                    var target_input = inputId_clueId[key][i];
                    document.getElementById(target_input).style.backgroundColor = "yellow";
                }
            }
        }
    }

    for (const [key, value] of Object.entries(inputId_clueId)) {
        var target = document.getElementsByClassName(key)[0];
        target.addEventListener('click', handleClick);


    }





});
socket.on('test', function (message) {
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

    socket.emit('time', { 'startTime': startTime });
}

function endgame() {
    stop_timer(); // Stop the timer
    let endTime = new Date().getTime(); // Get the current time in milliseconds
    socket.emit('time', { 'endTime': endTime });
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

