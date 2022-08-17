const boxes = document.querySelectorAll('.box1, .box2, .box3, .box4');

for (const box of boxes) {
  box.addEventListener('click', function handleClick() {
    box.classList.add('active');
  });
}