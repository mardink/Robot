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
				// Create a button to call Tilt Up macro
                var tiltupButton = webiopi().createButton("Tiltup", "Tilt Up", function() {
                   
                    // Call the macro
                    webiopi().callMacro("tilt_up");
                });
				// Create a button to call Tilt Neutral macro
                var tiltneutralButton = webiopi().createButton("Tiltneutral", "Neutral", function() {
                   
                    // Call the macro
                    webiopi().callMacro("tilt_neutral");
                });
				// Create a button to call Tilt down macro
                var tiltdownButton = webiopi().createButton("Tiltdown", "Tilt Down", function() {
                   
                    // Call the macro
                    webiopi().callMacro("tilt_down");
                });
				// Create a button to call Reboot macro
                var rebootButton = webiopi().createButton("Reboot", "Reboot", function() {
                   
                    // Call the macro
                    webiopi().callMacro("reboot");
                });
				// Create a button to call Reboot macro
                var shutdownButton = webiopi().createButton("Shutdown", "Shutdown", function() {
                   
                    // Call the macro
                    webiopi().callMacro("shutdown");
                });
				
				//Refresh the raspberry pi camera picture every 40ms =25fps
				setInterval(function(){
							$("#mjpeg_dest").attr("src", "stream/cam.jpg?"+new Date().getTime());
							},100);

                // Append the button to the controls box using a jQuery function
				//$("#TiltButtons").append(shutdownButton);
				//$("#TiltButtons").append(rebootButton);
				$("#TiltButtons").append(tiltupButton);
				$("#TiltButtons").append(tiltneutralButton);
				$("#TiltButtons").append(tiltdownButton);
                $("#PanLeftButton").append(panleftButton);
				$("#PanNeutralButton").append(panneutralButton);
				$("#PanRightButton").append(panrightButton);
				$("#Panleft").attr("class", "btn btn-success");
				$("#Panneutral").attr("class", "btn btn-primary");
				$("#Panright").attr("class", "btn btn-success");
				$("#Tiltup").attr("class", "btn btn-success");
				$("#Tiltneutral").attr("class", "btn btn-primary");
				$("#Tiltdown").attr("class", "btn btn-success");

                // Refresh GPIO buttons
                // pass true to refresh repeatedly of false to refresh once
                webiopi().refreshGPIO(true);

        });