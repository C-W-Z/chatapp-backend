/*=============== SHOW HIDDEN - PASSWORD ===============*/
const showHiddenPass = (formPass, formEye) => {
   const input = document.getElementById(formPass),
      iconEye = document.getElementById(formEye)

   iconEye.addEventListener('click', () => {
      // Change password to text
      if (input.type === 'password') {
         // Switch to text
         input.type = 'text'

         // Icon change
         iconEye.classList.add('ri-eye-line')
         iconEye.classList.remove('ri-eye-off-line')
      } else {
         // Change to password
         input.type = 'password'

         // Icon change
         iconEye.classList.remove('ri-eye-line')
         iconEye.classList.add('ri-eye-off-line')
      }
   })
}

showHiddenPass('form-pass', 'form-eye')
