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
            // console.log(typeof tdofnexttr);
            // console.log(tdofnexttr);

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

for (var i = 0; i < blocked_cell_list.length; i++) {
    document.getElementById(blocked_cell_list[i]).disabled = true;
    document.getElementById(blocked_cell_list[i]).closest('td').style.backgroundColor = "black";
}
