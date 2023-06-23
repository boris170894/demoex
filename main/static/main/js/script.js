var modal = document.getElementById('myModal');


let img_id;
const get_id = (id_img) => {
    console.log(id_img)
    var img = document.getElementById(id_img);
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    img.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    }


    var span = document.getElementsByClassName("close")[0];


    span.onclick = function() { 
        modal.style.display = "none";
    }
}




