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
				
				// Functions for driving
				// Create a button to call ForwardLeft macro
                var ForwardLeftButton = webiopi().createButton("Forwardleft", "Left", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Forward_left");
                });
				
				// Create a button to call forward macro
                var ForwardButton = webiopi().createButton("Forward", "Forward", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Forward");
                });
				
				// Create a button to call forwardRight macro
                var ForwardRightButton = webiopi().createButton("Forwardright", "Right", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Forward_right");
                });
				// Create a button to call forwardRight macro
                var StopButton = webiopi().createButton("Stop", "Stop", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Stop");
                });
				
				// Create a button to call BackwardLeft macro
                var BackwardLeftButton = webiopi().createButton("Backwardleft", "Left", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Backwards_left");
                });
				
				// Create a button to call forward macro
                var BackwardButton = webiopi().createButton("Backward", "Backward", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Backwards");
                });
				
				// Create a button to call forwardRight macro
                var BackwardRightButton = webiopi().createButton("Backwardright", "Right", function() {
                   
                    // Call the macro
                    webiopi().callMacro("Backwards_right");
                });
				
				//System Fucntions
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
				
				//Refresh the raspberry pi camera picture every 100ms 
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
				$("#ForwardButton").append(ForwardButton);
				$("#ForwardLeftButton").append(ForwardLeftButton);
				$("#ForwardRightButton").append(ForwardRightButton);
				$("#BackwardButton").append(BackwardButton);
				$("#BackwardLeftButton").append(BackwardLeftButton);
				$("#BackwardRightButton").append(BackwardRightButton);
				$("#StopButton").append(StopButton);
				$("#Panleft").attr("class", "btn btn-success");
				$("#Panneutral").attr("class", "btn btn-primary");
				$("#Panright").attr("class", "btn btn-success");
				$("#Tiltup").attr("class", "btn btn-success");
				$("#Tiltneutral").attr("class", "btn btn-primary");
				$("#Tiltdown").attr("class", "btn btn-success");
				$("#ForwardButton").attr("class", "btn btn-success");
				$("#ForwardLeftButton").attr("class", "btn btn-success");
				$("#ForwardRightButton").attr("class", "btn btn-success");
				$("#BackwardButton").attr("class", "btn btn-success");
				$("#BackwardLeftButton").attr("class", "btn btn-success");
				$("#BackwardRightButton").attr("class", "btn btn-success");
				$("#StopButton").attr("class", "btn btn-danger");

                // Refresh GPIO buttons
                // pass true to refresh repeatedly of false to refresh once
                webiopi().refreshGPIO(true);

        });
