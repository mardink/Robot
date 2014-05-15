webiopi().ready(function() {
                               
                // Create a button to call Pan Left macro
                var panleftButton = webiopi().createButton("Panleft", "Pan Left", function() {
                   
                    // Call the macro
                    webiopi().callMacro("pan_left");
                });
				// Create a button to call Pan Neutral macro
                var panneutralButton = webiopi().createButton("Panneutral", "Neutral", function() {
                   
                    // Call the macro
                    webiopi().callMacro("pan_neutral");
                });
				// Create a button to call Pan Right macro
                var panrightButton = webiopi().createButton("Panright", "Pan Right", function() {
                   
                    // Call the macro
                    webiopi().callMacro("pan_right");
                });
				
				//Refresh the raspberry pi camera picture every 40ms =25fps
				setInterval(function(){
							$("#mjpeg_dest").attr("src", "stream/cam.jpg?"+new Date().getTime());
							},100);

                // Append the button to the controls box using a jQuery function
                $("#controls").append(panleftButton);
				$("#controls").append(panneutralButton);
				$("#controls").append(panrightButton);

                // Refresh GPIO buttons
                // pass true to refresh repeatedly of false to refresh once
                webiopi().refreshGPIO(true);

        });