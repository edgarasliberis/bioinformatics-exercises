%% Digital Signal Processing #1
% Edgar Liberis, |el398@cam.ac.uk|

%% 
% *Exercise 1.*  
%
% # non-linear, time-invariant, causal, memory-less;
% # linear, time-invariant, non-causal;
% # non-linear, time-invariant, causal;
% # linear, non-time-invariant, non-causal;
% # non-linear, time-invariant, causal;
% # linear, non-time-invariant, causal, memory-less;
% # linear, time-invariant, causal, memory-less;
% # linear, non-time-invariant, non-causal;

%% 
% *Exercise 5*

% a) a * b = c 
% 
% where a = [-3, 2, 1]
% 
%      |-3     0     0     0     0 |
%      | 2    -3     0     0     0 |
%      | 1     2    -3     0     0 |
% a* = | 0     1     2    -3     0 |
%      | 0     0     1     2    -3 |
%      | 0     0     0     1     2 |
%      | 0     0     0     0     1 |

% b)
b = [1; 0; 0; 2; 2];
A_star = toeplitz([-3, 2, 1, 0, 0, 0, 0], [-3, 0, 0, 0, 0]);
c = (A_star * b)' % Transpose for printing in 1 row

c_conv = conv([-3, 2, 1], [1, 0, 0, 2, 2])

% c) Solving for b
b_solved = round(linsolve(A_star, c'))'

%%
% *Exercise 7* 
%
% Behaviour of holding the pulse for some time is equivalent to 
% mathematically multiplying sampled signal (comb of different heights),
% with a rectangle function, producing a kind of a step function.
%
% In frequency domain, this is equivalent to convolving the FT of the 
% sampled signal (also a comb) with sinc function (FT of rectangle func.),
% so the spectrum becomes a set of superimposed sinc functions. 
%

%%
% *Exercise 10*
% 

% a)
% 1 sec long 300Hz Gaussian noise
noise = randn(300, 1); % Isn't randn uniform, as opposed to Gaussian?

% Band-pass filter of 45Hz cut-off
f45 = fir1(50, 45/150);
x = filtfilt(f45, 1, noise);

% Sample X at 100Hz
y = zeros(1, 300);
y(1:3:end) = x(1:3:end);

% Band-pass filter of 50Hz cut-off
f50 = fir1(50, 50/150);
z = filtfilt(f50, 1, y) .* 3; % Compensate energy loss

hFig = figure(1);
set(hFig, 'Position', [20 20 1000 600])
plot(x, 'b'); hold on;
plot(y, 'r'); hold on;
plot(z, 'g');
legend('x_n = 45Hz bandpassed 300Hz noise', ...
       'y_n = x_n sampled at 100Hz', ...
       'z_n = 50Hz bandpassed y_n');
   
% x_n and z_n almost don't differ.

% b) So that the second filter doesn't discard useful information. 
% Bandpassing signal whose highest frequency is 45Hz with a 50Hz
% filter would have no effect.
