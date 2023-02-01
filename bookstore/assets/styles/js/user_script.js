const displayPage = (param) => {
  const profile = document.getElementById('profile');
  const books = document.getElementById('books');
  const changePass = document.getElementById('change_password');
  switch (param){
      case 'profile':
          {
          profile.style.display = 'block'
          books.style.display = 'none'
          changePass.style.display = 'none'
          break; 
          }
          case 'chp':
              {
              profile.style.display = 'none'
              books.style.display = 'none'
              changePass.style.display = 'block'
              break
              }
      case 'books':
          {
          profile.style.display = 'none'
          books.style.display = 'block'
          changePass.style.display = 'none'
          break
          }
  }
}


const imgDiv = document.querySelector('#upload-img-div');
const img = document.querySelector('#uploadImage');
const file = document.querySelector('#file');
const uploadBtn = document.querySelector('#uploadBtn');

imgDiv.addEventListener('mouseenter', () => {
  uploadBtn.style.display = 'block';
})
imgDiv.addEventListener('mouseleave', () => {
  uploadBtn.style.display = 'none';
})

file.addEventListener('change', function() {
  const chosenFile = this.files[0];
  if (chosenFile) {
    const reader = new FileReader();

    reader.addEventListener('load', () => {
      img.setAttribute('src', reader.result);
    })

    reader.readAsDataURL(chosenFile);
  }
})


