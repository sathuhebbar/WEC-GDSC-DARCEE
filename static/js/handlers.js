/* THESE FUNCTIONS ARE UGLY */

/*
 * Called when dark mode has to be enabled/disabled
 */
function dark_mode_change() {
    v = document.getElementsByTagName('textarea')[0]
    white = "rgb(255, 255, 255)"
    black = "rgb(0, 0, 0)"
    monokai_bg = "rgb(39, 40, 34)"
    c = window.getComputedStyle(v).getPropertyValue("background-color")
    if (c == "rgb(255, 255, 255)") {
        for (const x of document.getElementsByTagName('span'))
            x.style.color = white
        for (const x of document.getElementsByTagName('body'))
            x.style.backgroundColor = monokai_bg
        for (const x of document.getElementsByTagName('textarea')) {
            x.style.backgroundColor = monokai_bg
            x.style.color = white
        }
        x = document.getElementsByName('lang')[0]
        x.style.backgroundColor = monokai_bg
        x.style.color = white

    } else {
        for (const x of document.getElementsByTagName('span'))
            x.style.color = black
        for (const x of document.getElementsByTagName('body'))
            x.style.backgroundColor = white
        for (const x of document.getElementsByTagName('textarea')) {
            x.style.backgroundColor = white
            x.style.color = black
        }
        x = document.getElementsByName('lang')[0]
        x.style.backgroundColor = white
        x.style.color = black

    }
}

/*
 * Called on button click to copy source/input/output/error.
 */
function copy_button(x) {
    p = navigator.clipboard
    c = document.getElementById(x)
    p.writeText(c.value).then(() => alert('Copied!'))
}

/*
 * Called to change font size.
 */
function change_font_size() {
    d = document.getElementById('font_size_select')
    for (const x of document.getElementsByTagName('textarea'))
        x.style.fontSize = d.value + "px"
}