// Called when dark mode has to be enabled/disabled
function dark_mode_change() {

    // UGLY FUNCTION
    v = document.getElementById('source_area')
    c = window.getComputedStyle(v).getPropertyValue("background-color")
    if (c == "rgb(255, 255, 255)") {
        for (const x of document.getElementsByTagName('label'))
            x.style.color = "rgb(255, 255, 255)"
        for (const x of document.getElementsByTagName('body'))
            x.style.backgroundColor = "rgb(33, 37, 41)"
        for (const x of document.getElementsByTagName('textarea')) {
            x.style.backgroundColor = "rgb(33, 37, 41)"
            x.style.color = "rgb(255, 255, 255)"
        }
        for(const x of document.getElementsByTagName('select')) {
            x.style.backgroundColor = "rgb(33, 37, 41)"
            x.style.color = "rgb(255, 255, 255)"
        }
    }
    else {
        for (const x of document.getElementsByTagName('label'))
            x.style.color = "rgb(0, 0, 0)"
        for (const x of document.getElementsByTagName('body'))
            x.style.backgroundColor = "rgb(255, 255, 255)"
        for (const x of document.getElementsByTagName('textarea')) {
            x.style.backgroundColor = "rgb(255, 255, 255)"
            x.style.color = "rgb(0, 0, 0)"
        }
        for(const x of document.getElementsByTagName('select')) {
            x.style.backgroundColor = "rgb(255, 255, 255)"
            x.style.color = "rgb(0, 0, 0)"
        }
    }
}

