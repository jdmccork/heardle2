var length = 1

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function pauseCheck() {
    var current_song = document.getElementById('player')
    if (current_song.currentTime > length) {
        current_song.pause()
    }
}

function playSong() {
    var current_song = document.getElementById('player')
    current_song.currentTime = 0
}

function play() {
    let game = document.getElementById('game')
    game.hidden = true

    let player = document.getElementById('player')
    
    fetch("/selectSong").then(response => response.json()).then(data => {
        let title = data.title
        let artist = data.artist
        let url = data.url

        player.setAttribute('src', "/track?track_url=" + encodeURIComponent(url))
        
        let titleElement = document.getElementById('trackTitle')
        titleElement.textContent = title
        
        let artistElement = document.getElementById('trackArtist')
        artistElement.textContent = artist
    }).then(() => {
        game.hidden = false
    })
    
}