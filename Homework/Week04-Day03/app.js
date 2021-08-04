let btnLeft=document.querySelector('.btn-left')
let btnUp=document.querySelector('.btn-up')
let btnRight=document.querySelector('.btn-right')
let btnDown=document.querySelector('.btn-down')
let Box=document.querySelector('.boxc')
marginAmount1=0
marginAmount2=0
marginAmount3=0
marginAmount4=0

btnLeft.addEventListener('click',function(){
  let Move=document.querySelector('.box').style.marginRight =`${marginAmount1}px` ;
  marginAmount1+=20
  let animation=document.querySelector('.box').style.transition = "all 0.9s";

})

btnUp.addEventListener('click',function(){
    let Move=document.querySelector('.box').style.marginTop = `${marginAmount2}px`;
    marginAmount2+=-20
    let animation=document.querySelector('.box').style.transition = "all 0.9s";

  })

  btnRight.addEventListener('click',function(){
    let Move=document.querySelector('.box').style.marginLeft = `${marginAmount3}px`;
    marginAmount3+=20
    let animation=document.querySelector('.box').style.transition = "all 0.9s";

  })

  btnDown.addEventListener('click',function(){
    let Move=document.querySelector('.box').style.marginTop =`${marginAmount4}px` ;
    marginAmount4+=20
    let animation=document.querySelector('.box').style.transition = "all 0.9s";


  })
 