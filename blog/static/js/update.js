function changeVis() {
    var window = document.querySelector('.update_window');
    var button = document.querySelector('.settings');
    var window_state = window.style.opacity;
    
    if (window_state == 0) {
        window.style.opacity = 9;
    }
    else {
        window.style.opacity = 0;
        
    }
}