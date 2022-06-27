let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/stokkel-72-927kb.jpg') {
        myImage.setAttribute('src','images/stokkel-65.jpg');
    } else {
        myImage.setAttribute('src','images/stokkel-72-927kb.jpg');
    }
}