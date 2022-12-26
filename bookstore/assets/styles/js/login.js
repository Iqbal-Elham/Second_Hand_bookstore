const displayForm = (section) => {
const signInForm = document.querySelector('#sign-in-form')
const signUpForm = document.querySelector('#sign-up-form')
if (section === 'sign-in') {
  signInForm.style.display = 'block'
  signUpForm.style.display = 'none'
}
if (section === 'sign-up') {
  signInForm.style.display = 'none'
  signUpForm.style.display = 'block'
}
}