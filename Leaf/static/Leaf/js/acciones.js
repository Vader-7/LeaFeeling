$(document).ready(function(){
//FUNCIONALIDAD CATALOGO MACETEROS
    $("#hide1").click(function (e) {
        e.preventDefault();
        $("#div1").hide(1000);
    })
    $("#hide1").click(function(){
        $("#descripcion1").show(1000);
    });
    $("#catalogo1").click(function (e) {
        e.preventDefault();
        $("#div1").show(1000);
    })
    $("#catalogo1").click(function (e) {
        e.preventDefault();
        $("#descripcion1").hide(1000);
    })
//FUNCIONALIDAD CATALOGO SEMILLAS
    $("#hide2").click(function (e) {
        e.preventDefault();
        $("#div1").hide(1000);
    })
    $("#hide2").click(function(){
        $("#descripcion2").show(1000);
    });
    $("#catalogo2").click(function (e) {
        e.preventDefault();
        $("#div1").show(1000);
    })
    $("#catalogo2").click(function (e) {
        e.preventDefault();
        $("#descripcion2").hide(1000);
    })
//FUNCIONALIDAD CATALOGO FERTILIZANTES
    $("#hide3").click(function (e) {
        e.preventDefault();
        $("#div1").hide(1000);
    })
    $("#hide3").click(function(){
        $("#descripcion3").show(1000);
    });
    $("#catalogo3").click(function (e) {
        e.preventDefault();
        $("#div1").show(1000);
    })
    $("#catalogo3").click(function (e) {
        e.preventDefault();
        $("#descripcion3").hide(1000);
    })
//FUNCIONALIDAD MACETERO 1
    $("#mac_img1").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_des1, #mac_com1").show(1000);
    })
    $("#mac_img1").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_img1").hide(1000);
    })
    $("#mac_des1").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_img1").show(1000);
    })
    $("#mac_des1").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_des1").hide(1000);
    })
//FUNCIONALIDAD MACETERO 2
    $("#mac_img2").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_des2, #mac_com2").show(1000);
    })
    $("#mac_img2").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_img2").hide(1000);
    })
    $("#mac_des2").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_img2").show(1000);
    })
    $("#mac_des2").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_des2").hide(1000);
    })
//FUNCIONALIDAD MACETERO 3
    $("#mac_img3").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_des3, #mac_com3").show(1000);
    })
    $("#mac_img3").mouseenter(function (e) {
        e.preventDefault();
        $("#mac_img3").hide(1000);
    })
    $("#mac_des3").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_img3").show(1000);
    })
    $("#mac_des3").mouseleave(function (e) {
        e.preventDefault();
        $("#mac_des3").hide(1000);
    })
//FUNCIONALIDAD COMPRA GENERAL
    $("#mac_com1").click(function (e) {
        e.preventDefault();
        $("#mac_descrip1, #mac_catalogo, #web_pay, #carrito").show(1000);
    })
    $("#mac_com1").click(function (e) {
        e.preventDefault();
        $("#maceteros").hide(1000);
    })
    $("#mac_catalogo").click(function (e) {
        e.preventDefault();
        $("#maceteros").show(1000);
    })
    $("#mac_catalogo").click(function (e) {
        e.preventDefault();
        $("#mac_descrip1, #mac_descrip2, #mac_descrip3, #mac_catalogo, #web_pay, #carrito").hide(1000);
    })
    $("#mac_com2").click(function (e) {
        e.preventDefault();
        $("#mac_descrip2, #mac_catalogo2, #web_pay, #carrito").show(1000);
    })
    $("#mac_com2").click(function (e) {
        e.preventDefault();
        $("#maceteros").hide(1000);
    })
    $("#mac_catalogo2").click(function (e) {
        e.preventDefault();
        $("#maceteros").show(1000);
    })
    $("#mac_catalogo2").click(function (e) {
        e.preventDefault();
        $("#mac_descrip1, #mac_descrip2, #mac_descrip3,#mac_catalogo2,  #web_pay, #carrito").hide(1000);
    })
    $("#mac_com3").click(function (e) {
        e.preventDefault();
        $("#mac_descrip3, #mac_catalogo3, #web_pay, #carrito").show(1000);
    })
    $("#mac_com3").click(function (e) {
        e.preventDefault();
        $("#maceteros").hide(1000);
    })
    $("#mac_catalogo3").click(function (e) {
        e.preventDefault();
        $("#maceteros").show(1000);
    })
    $("#mac_catalogo3").click(function (e) {
        e.preventDefault();
        $("#mac_descrip1, #mac_descrip2, #mac_descrip3, #mac_catalogo3, #web_pay, #carrito").hide(1000);
    }) 
});

