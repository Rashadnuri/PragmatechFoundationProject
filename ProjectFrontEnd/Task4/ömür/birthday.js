// let d1= new Date()
// let d2= new Date(2001, 12, 16)

// let time= new Date(d1.getTime() - d2.getTime())
// let years= time.getFullYear()
// let days= time.getDay
// let hour= time.getHours
// let minutes= time.getMinutes
// let second= time.getSeconds
// let msecons= time.getMilliseconds

// setInterval(()=>{
//     let d1=new Date()
//     let d2= new Date(2001, 12, 16)
//     let btn=document.querySelector('.btn')
//     btn.innerHTML= `${d.getHours()} : ${d.getMinutes()}: ${d.getSeconds()}: ${d.getMilliseconds()}`
// },1)

setInterval(()=>{

    let currentDate = new Date()
    let birthday = new Date('12 16, 2001 11:15:00')
    let currentYear = currentDate.getFullYear()
    let birthdayYear = birthday.getFullYear()
    let currentMonth = currentDate.getMonth()
    let birthdayMonth = birthday.getMonth()
    let currentDay = currentDate.getDate()
    let birthdayDay = birthday.getDate()
    
    let bday=3
    let age = Math.abs(currentYear-birthdayYear-1)
    let month = Math.abs(currentMonth)
    let day = Math.abs(31-birthdayDay+5)
    
    let btn=document.querySelector('.btn')
    
    btn.innerHTML=`${age + "Year"} ${month+ "Month"}  ${day + "Days" } ${currentDate.getHours() + 'Hours'} : ${currentDate.getMinutes()+'Minutes'}: ${currentDate.getSeconds()+ 'Seconds'}: ${currentDate.getMilliseconds()+'Milliseconds'}`
    },1)


