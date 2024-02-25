$(document).ready(function () {
    $("input").keyup(function (e) {
        if (e.which == 39) {
            // right arrow
            $(this)
                .closest("td")
                .nextAll("td:not(:has(input[disabled])):first")
                .find("input")
                .focus();
        } else if (e.which == 37) {
            // left arrow
            $(this)
                .closest("td")
                .prevAll("td:not(:has(input[disabled])):first")
                .find("input")
                .focus();
        } else if (e.which == 40) {
            // down arrow

            var currentIndex = $(this).closest("td").index();
            var nextRow = $(this).closest("tr").next("tr");
            var tdofnexttr = nextRow.find("td:eq(" + currentIndex + ")");
            console.log("helo helo");
            console.log(typeof tdofnexttr);
            console.log(tdofnexttr);

            while (tdofnexttr.length > 0) {
                if (!tdofnexttr.find("input").prop("disabled")) {
                    tdofnexttr.find("input").focus();
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
                    tdofprevtr.find("input").focus();
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
    });
});



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}




async function delayedLoop() {
    for (const key in order) {
        let x = order[key][0];
        let y =  order[key][1];
        let prefix = "input";
        let id = prefix + x + "-" + y;
        if (grid[x][y] != "") {
            var delay = 50;
            await sleep(delay);
            document.getElementById(id).value = grid[x][y];
        
    };

    };           
     
}





// delayedLoop();

