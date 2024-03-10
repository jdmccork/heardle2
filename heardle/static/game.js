var length = 1

function pauseCheck() {
    var current_song = document.getElementById('song')
    console.log(current_song.currentTime)
    if (current_song.currentTime > length) {
        current_song.pause()
    }
}

function playSong() {
    var current_song = document.getElementById('song')
    current_song.currentTime = 0
}