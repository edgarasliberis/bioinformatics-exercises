%% Digital Signal Processing #2
% Edgar Liberis, |el398@cam.ac.uk|

%% 
% *Exercise 12.*  

f = fopen('iq-fm-96M-240k.dat', 'r', 'ieee-le');
c = fread(f, [2,inf], '*float32');
fclose(f);
z = c(1,:) + 1i*c(2,:);

% FM demodulate the signal
f = 240000;
s = angle(z(2:end) ./ z(1:end-1)) * f;

% Apply a low-pass 16kHz filter
[filtB, filtA] = butter(9, 16000/(f/2), 'low');
filtered = filter(filtB, filtA, s);

% Reduce sampling rate to 48kHz
reduced = filtered(1:5:end);

% Normalise amplitude by dividing each sample by maximum amplitude
normCoeff = max(abs(max(reduced)), abs(min(reduced)));
normalised = reduced ./ normCoeff;

% Output the file
audiowrite('ex12.wav', normalised, 48000); 

%%
% *Exercise 14.*
%
% DFT is a transform, that defines Fourier coefficients for a signal.
% FFT is an algorithm for computing DFT coefficients.
% FFTW is a particular implementation of FFT, which claims to have high
% performance.

%% 
% *Exercise 16.*
%
% a) Index 0 would correspond to the DC component (0 Hz), and indices would
% be separated by 8000 Hz / 256 = 31.25 Hz bands, i.e. index i would
% correspond to i*31.25 Hz.
%
% 9 would send 852Hz and 1477Hz tones, which corresponds to indices
% 27 (= 852Hz / 31.25Hz) and 47 (= 1477Hz / 31.25Hz)
%
% b)

% Read input file and the sampling frequency
[y, fs] = audioread('touchtone.wav');

% Compute the spectrogram for specified frequencies only
% (makes it easier to read off, 1075Hz, 1800 are dummy values to get an
% extra band)
freqs = [697, 770, 852, 941, 1075, 1209, 1336, 1477, 1633, 1800];

figure(1)
spectrogram(y, 512, 256, freqs, fs, 'yaxis');

figure(2) % Full histogram, for reference
spectrogram(y, 512, 'yaxis'); 

% Recovered: 900441223334676 (Markus's Office Number)

%%
% *Exercise 17a*
%

% Constructing filters
freqs = [697, 770, 852, 941, 1209, 1336, 1477];

figure(3)
% Filter sequence using bandpass FIR filter for every frequency
for i = 1:length(freqs)
   f = fir1(50, [0.982 * freqs(i) / (fs/2), 1.018 * freqs(i) / (fs/2)], 'bandpass');
   filtered = filtfilt(f, 1, y);
   % Make values more visible
   plot((filtered .* 5000) + freqs(i)); hold on;
end

