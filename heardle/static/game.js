var length = 1

function pauseCheck() {
    var current_song = document.getElementById('player')
    console.log(current_song.currentTime)
    if (current_song.currentTime > length) {
        current_song.pause()
    }
}

function play() {
    let game = document.getElementById('game')
    game.hidden = false

    let player = document.getElementById('player')
    player.setAttribute('src', "http://127.0.0.1:5000/test");

}