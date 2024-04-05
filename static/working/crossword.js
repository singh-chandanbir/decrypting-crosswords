document.addEventListener('contextmenu', event => event.preventDefault());

$(document).ready(function () {
    $("input").keyup(function (e) {
        if (e.which == 39) {
            // right arrow
            $(this)
                .closest("td")
                .nextAll("td:not(:has(input[disabled])):first")
                .find("input")
                .trigger('click');
        } else if (e.which == 37) {
            // left arrow
            $(this)
                .closest("td")
                .prevAll("td:not(:has(input[disabled])):first")
                .find("input")
                .trigger('click');
        } else if (e.which == 40) {
            // down arrow
            var currentIndex = $(this).closest("td").index();
            var nextRow = $(this).closest("tr").next("tr");
            var tdofnexttr = nextRow.find("td:eq(" + currentIndex + ")");

            while (tdofnexttr.length > 0) {
                if (!tdofnexttr.find("input").prop("disabled")) {
                    tdofnexttr.find("input").trigger('click');
                    break;
                } else {
                    currentIndex = nextRow.find("td:eq(" + currentIndex + ")").index();
                    nextRow = nextRow
                        .find("td:eq(" + currentIndex + ")")
                        .closest("tr")
                        .next("tr");
                    tdofnexttr = nextRow.find("td:eq(" + currentIndex + ")");
                }
            }
        } else if (e.which == 38) {
            // up arrow
            var currentIndex = $(this).closest("td").index();
            var prevRow = $(this).closest("tr").prev("tr");
            var tdofprevtr = prevRow.find("td:eq(" + currentIndex + ")");

            while (tdofprevtr.length > 0) {
                if (!tdofprevtr.find("input").prop("disabled")) {
                    tdofprevtr.find("input").trigger('click');
                    break;
                } else {
                    currentIndex = prevRow.find("td:eq(" + currentIndex + ")").index();
                    prevRow = prevRow
                        .find("td:eq(" + currentIndex + ")")
                        .closest("tr")
                        .prev("tr");
                    tdofprevtr = prevRow.find("td:eq(" + currentIndex + ")");
                }
            }
        }
        else if (e.which == 8) {
            // backspace
            moveBack();

        }

        else if (e.which >= 65 && e.which <= 90) {
            // alphabets
            let character = String.fromCharCode(e.which);
            let current_input = document.getElementById(current_selected_inputs[current_focused_input_index]);
            current_input.value = character;
            moveAhead();

        }
    });
});

for (let i = 0; i < blocked_cell_list.length; i++) {
    let disabled_input = document.getElementById(blocked_cell_list[i]);
    disabled_input.disabled = true;
    disabled_input.closest('td').style.backgroundColor = "black";
}



function moveAhead() {
    if (current_focused_input_index >= 0 && current_focused_input_index < (current_selected_inputs.length - 1)) {
        let current_input = document.getElementById(current_selected_inputs[current_focused_input_index]);
        current_input.style.backgroundColor = "#f7f0a3";
        if ((current_focused_input_index + 1) < current_selected_inputs.length) {
            current_focused_input_index += 1;
            let next_input = document.getElementById(current_selected_inputs[current_focused_input_index]);
            next_input.focus();
            next_input.style.backgroundColor = "yellow";
        }
    }

}

function moveBack() {
    if (current_focused_input_index > 0) {
        let current_input = document.getElementById(current_selected_inputs[current_focused_input_index]);
        current_input.style.backgroundColor = "#f7f0a3";
        current_focused_input_index -= 1;
        let prev_input = document.getElementById(current_selected_inputs[current_focused_input_index]);
        prev_input.focus();
        prev_input.style.backgroundColor = "yellow";
    }

}

