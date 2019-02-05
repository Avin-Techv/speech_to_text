////start of app.js
//'use strict';
//
//var isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
//var wavesurfer, context, processor;
//
//// Init & load
//document.addEventListener('DOMContentLoaded', function() {
//    var micBtn = document.querySelector('#micBtn');
//
//    micBtn.onclick = function() {
//        if (wavesurfer === undefined) {
//            if (isSafari) {
//                // Safari 11 or newer automatically suspends new AudioContext's that aren't
//                // created in response to a user-gesture, like a click or tap, so create one
//                // here (inc. the script processor)
//                var AudioContext =
//                    window.AudioContext || window.webkitAudioContext;
//                context = new AudioContext();
//                processor = context.createScriptProcessor(1024, 1, 1);
//                startButton(event);
//            }
//
//            // Init wavesurfer
//            wavesurfer = WaveSurfer.create({
//                container: '#waveform',
//                waveColor: 'black',
//                interact: false,
//                cursorWidth: 0,
//                audioContext: context || null,
//                audioScriptProcessor: processor || null,
//                plugins: [WaveSurfer.microphone.create()]
//            });
//
//            wavesurfer.microphone.on('deviceReady', function() {
//                var image = document.getElementById('start_img');
//                var url = image.src;
//                url = url.split('#').pop().split('?').pop();
//                var image_name = url.substring(url.lastIndexOf('/') + 1);
//
//                if (image_name==="loader.gif"){
//                    var img1 = "../static/icon/mic.png";
//                    image.setAttribute('src', img1);
//                    wavesurfer.microphone.stop();
//                }
//                else{
//                    console.info('Device ready!');
//                    var image = document.getElementById('start_img');
//                    var img2 = "../static/icon/loader.gif";
//                    image.setAttribute('src', img2);
//                    //toggle_mic_image();
//                    //console.log("func called 1");
//                    startButton(event);
//                }
//            });
//            wavesurfer.microphone.on('deviceError', function(code) {
//                console.warn('Device error: ' + code);
//            });
//            wavesurfer.microphone.start();
//        } else {
//            // start/stop mic on button click
//            if (wavesurfer.microphone.active) {
//                wavesurfer.microphone.stop();
//                var image = document.getElementById('start_img');
//                console.log("before func called 2");
//                var img1 = "../static/icon/mic.png";
//                image.setAttribute('src', img1);
//                console.log("func called 2");
//                var recognizing = false;
//                startButton(event);
//            } else {
//                wavesurfer.microphone.start();
//                showInfo('info_start');
//                var image = document.getElementById('start_img');
//                var img2 = "../static/icon/loader.gif";
//                image.setAttribute('src', img2);
//                startButton(event);
//            }
//        }
//    };
//});
////end of app.js