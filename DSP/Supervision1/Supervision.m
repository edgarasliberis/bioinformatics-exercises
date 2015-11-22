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

% c)

conv([-3, 2, 1], [1, 0, 0, 2, 2])

%%
% *Exercise 7* 
%
% Behaviour of holding the pulse for the constant is equivalent to 
% mathematically multiplying sampled signal (comb of different heights),
% by a rectangle function, producing a kind of a step function.
%
% In frequency domain, this is equivalent to convolving the FT of the 
% sampled signal (also a comb) with sinc function (FT of rectangle func.),
% so spectrum becomes a set of superimposed sinc functions. 
%

%%
% *Exercise 10*
% 
