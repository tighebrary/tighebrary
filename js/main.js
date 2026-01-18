// For taking the color of text, giving it that color background, and turning text white
      document.querySelectorAll('.dynamic-link').forEach(link => {
          link.addEventListener('mouseenter', function() {
              const initialColor = window.getComputedStyle(this).color;
              fixedColor = initialColor
              this.style.backgroundColor = initialColor;
              this.style.color = 'white'; // Change text color to white
          });

          link.addEventListener('mouseleave', function() {
              this.style.backgroundColor = 'transparent';
              this.style.color = fixedColor; // Reset to initial color
          });
      });
