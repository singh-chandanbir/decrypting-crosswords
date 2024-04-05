// some global variables
var timer;
let red = "#ff7e75";
let green = "#65ed55";
// data from the server
var grid;
var order;
var inputId_clueId;


// // current selected input and direction
var current_selected_inputs = {};
// var current_selected_direction = "";
var current_focused_input_index = null;

// //previously selected input and direction
// var previosly_selected_direction = "";
var previosly_selected_input = {};


// FEF9C3


var socket = io();
socket.on('connect', function () {
});

socket.on('gameData', function (message) {
    grid = message['grid'];
    order = message['order'];
    inputId_clueId = message['inputId_clueId'];

});


function startgame() {
    timer = start_timer();
    makeCluesClickable();
    makeInputClickable();
    let startTime = new Date().getTime();
    socket.emit('time', { 'startTime': startTime });
}

function makeInputClickable() {
    document.getElementById("start-btn-wrapper").style.display = "none";
    document.getElementById("btn-wrapper").style.display = "flex";


    for (const [key, value] of Object.entries(inputId_clueId)) {
        for (let i = 0; i < value.length; i++) {
            let target = document.getElementById(value[i]);
            target.addEventListener('click', handleInputClick);
        }

    }

    function handleInputClick(event) {

        let selected_input = event.target.id;
        let found = false;

        for (const [key, value] of Object.entries(inputId_clueId)) {
            for (let i = 0; i < value.length; i++) {
                if (selected_input === value[i]) {
                    found = true;
                    for (const i in current_selected_inputs) {
                        document.getElementById(current_selected_inputs[i]).style.backgroundColor = "transparent";
                    }
                    previosly_selected_input = current_selected_inputs;
                    // previosly_selected_direction = current_selected_direction;

                    current_selected_inputs = value;
                    // current_selected_direction = key.split("-")[1];
                    current_focused_input_index = i;
                    for (let i = 0; i < value.length; i++) {
                        var target_input = value[i];
                        document.getElementById(target_input).style.backgroundColor = "#f7f0a3";
                    }
                    document.getElementById(selected_input).focus();
                    document.getElementById(selected_input).style.backgroundColor = "yellow";
                    break;
                }

            }
            if (found == true) {
                break;
            }
        }
    }

}

function makeCluesClickable() {
    function handleClueClick(event) {
        previosly_selected_input = current_selected_inputs
        // previosly_selected_direction = current_selected_direction;
        for (let i = 0; i < previosly_selected_input.length; i++) {
            document.getElementById(previosly_selected_input[i]).style.backgroundColor = "transparent";
        }
        let selected_clue = event.target.className;
        for (const key in inputId_clueId) {
            if (key === selected_clue) {
                current_selected_inputs = inputId_clueId[key];
                // current_selected_direction = key.split("-")[1];
                let start_input = inputId_clueId[key][0];
                current_focused_input_index = 0;
                document.getElementById(start_input).focus();
                document.getElementById(start_input).style.backgroundColor = "yellow";
                for (let i = 1; i < inputId_clueId[key].length; i++) {
                    let target_input = inputId_clueId[key][i];
                    document.getElementById(target_input).style.backgroundColor = "#f7f0a3";
                }
            }
        }
    }

    for (const [key, value] of Object.entries(inputId_clueId)) {
        let target = document.getElementsByClassName(key)[0];
        target.addEventListener('click', handleClueClick);
    }
}

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
    return timer;
}


function stop_timer() {
    clearInterval(timer);
}

function checkAll() {


    // let correct = true;
    // let incorrect_words = 0;
    // let total_words = 0;

    // for (const [key, value] of Object.entries(inputId_clueId)) {


    //     for (let i = 0; i < value.length; i++) {
    //         let id = value[i];
    //         let temp = id.split("-")[0];
    //         let x = parseInt(temp.split("input")[1]);
    //         let y = parseInt(id.split("-")[1]);
    //         if (document.getElementById(id).value == "") {
    //             continue;
    //         }
    //         else {
    //             console.log("id", id);  
    //             if (grid[x][y] != document.getElementById(id).value) {
    //                 console.log("x,y" ,x ,y)
    //                 incorrect_words += 1;
    //                 break;
    //             }

    //         }

    //     }
    //     total_words += 1;
    // }
    // console.log("total_words", total_words);

    // console.log('incorrect_words', incorrect_words);
    let inputboxs = document.getElementsByClassName("inputbox");

    for (const iterator of inputboxs) {
        let id = iterator.id;

        let temp = id.split("-")[0];
        let x = parseInt(temp.split("input")[1]);
        let y = parseInt(id.split("-")[1]);
        if (iterator.value == "") {
            continue;
        }
        else {
            if (grid[x][y] != iterator.value) {
                document.getElementById(id).style.backgroundColor = red;
            } else {
                document.getElementById(id).style.backgroundColor = green;
            }
        }

    }


    // make words from grid

    let word_list_user = [];
    let word_list = [];
    let correct_words = 0;
    for (const [key, value] of Object.entries(inputId_clueId)) {

        let word = "";
        let user_word = "";
        for (let i = 0; i < value.length; i++) {
            let id = value[i];
            let temp = id.split("-")[0];
            let x = parseInt(temp.split("input")[1]);
            let y = parseInt(id.split("-")[1]);
            word += grid[x][y];
            user_word += document.getElementById(id).value;

        }
        word_list.push(word);
        word_list_user.push(user_word);

    }
    for (let i = 0; i < word_list.length; i++) {
        if (word_list[i] === word_list_user[i]) {
            correct_words += 1;
            
        }
    }

    console.log("word_list", word_list);
    console.log("word_list_user", word_list_user);

    console.log("correct_words", correct_words);
    console.log("total_words", word_list.length);
    accuracy = (correct_words / word_list.length) * 100;
    console.log("accuracy", accuracy);





}

function abortgame() {

}
function endgame() {
    stop_timer();
    let endTime = new Date().getTime();
    socket.emit('time', { 'endTime': endTime });
}

function clearAll() {
    let inputboxs = document.getElementsByClassName("inputbox");
    for (const iterator of inputboxs) {
        iterator.value = "";
        iterator.style.backgroundColor = "transparent";
    }
}

function clearSelected() {
    for (const i in current_selected_inputs) {
        document.getElementById(current_selected_inputs[i]).value = "";
        document.getElementById(current_selected_inputs[i]).style.backgroundColor = "#f7f0a3";
    }

    document.getElementById(current_selected_inputs[0]).focus();
    document.getElementById(current_selected_inputs[0]).style.backgroundColor = "yellow";
    current_focused_input_index = 0;
}




async function revealAll() {
    clearAll();
    var bot = document.getElementById("think");
    endgame();

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

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}