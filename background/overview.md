# Overview of the experiment and dataset
Based on the technical white paper: https://portal.brain-map.org/circuits-behavior/visual-behavior-2p

The goal of the project is to understand how neural activity in the visual cortex is related to behavior and sensory stimuli. To achieve this, the 2-photon calcium
imaging method (see file calcium_imaging_method_explanation.md) was used to measure the activity of different neurons (e.g., VIP and SST neurons, see file
vip_sst_neurons_background.md) in mice performing a visual task. The entire experiment involved 82 mice and 3021 training sessions. A total of 551 imaging sessions were
conducted, capturing activity from 34,619 cells. The scale of this experiment underscores the meticulous design required to ensure reliable and reproducible results
across a wide variety of conditions. These large datasets also allow for robust statistical analyses to uncover subtle neural and behavioral patterns.

## Task & Experiment Design
Before the experiment, the mice were trained for their task.
1. First, they learned to detect orientation using static grating patterns.
2. Next, they were introduced to flashing grating stimuli.
3. Finally, they learned to detect changes in natural scene images, which is the main task of the experiment.

The visual task for the experiment is a change detection task (a go/no-go task). In this task, mice are presented with a continuous series of images and earn a water
reward if they correctly identify when an image changes. The mice learn to lick a spout to indicate their detection of the change. If the image does not change, but the
mouse reacts as if it did, this is also recorded, allowing researchers to capture both correct and incorrect responses. Each session uses 8 different images selected
from a predefined pool of natural scenes. These images are chosen to provide variety while ensuring consistency across sessions. In addition to the individual images,
the experimental design incorporates 64 transition pairs, which refer to the specific switch from one image to another. This means that every image change is
pre-defined as part of a pair, ensuring that transitions are not random but systematically controlled. Choosing 64 pairs from the possible image transitions ensures
that the experiments cover various combinations of transitions while maintaining some standardization. By standardizing the transition pairs, researchers can compare
mouse responses under similar conditions, identify patterns in their detection accuracy, and analyze how specific image transitions affect neural activity. This design
also helps in examining whether certain transitions are inherently more challenging for the mice or evoke distinct patterns of brain activity compared to others. By
systematically adjusting these transitions, researchers can also test hypotheses about how environmental predictability influences learning and neural representation
formation. Moreover, the controlled nature of the task allows for a detailed investigation of how neural representations are formed and adjusted over time as the mice
gain experience with the task or encounter novel transitions. This approach provides insights into how the brain processes changes in the sensory environment and adapts
behavior accordingly.
During imaging sessions, mice are shown both familiar images (from their training) and new images (images they have never seen before). This helps researchers study the
effects of novelty on neural activity. Images are presented sequentially in a fixed timing pattern. An image is shown for a short time (250 ms), followed by a brief
pause before the next image appears. With a 5% probability, a stimulus in the sequence is omitted. Instead of a new image, the mice see a blank screen (= no stimulus)
or a neutral display during the planned presentation time. Mice quickly adapt to the regular sequence of stimuli. An omission breaks this expected sequence, creating an
unexpected situation that the brain may process differently. Stimulus omissions might also influence behavior, such as the licking response of the mice. Researchers can
analyze whether the mice are confused by the omission or adjust their expectations. Importantly, a stimulus change or the stimulus immediately before a change is never
omitted, ensuring that the mice can correctly detect changes. This keeps the mice's main task of detecting image changes intact.
There are also passive sessions, where the mice view the stimuli (images or image transitions) without performing a task and without the opportunity to earn a reward
(water). The mice are not actively engaged because they have already received their daily water allowance before the session. Additionally, the lick spouts are
retracted, so even if they want to lick, they cannot receive water. Stimuli are presented in a similar sequence to active sessions, including regular image changes and
stimulus omissions (5%). However, since the mice do not need to perform any behavior, the pure stimulus-driven neural activity can be studied. By comparing neural
responses in active and passive sessions, researchers can evaluate the influence of behavior and motivation. This comparative analysis is critical for disentangling the
neural mechanisms underlying voluntary attention from those activated by mere sensory stimulation. Understanding these distinctions can inform broader theories of
sensory processing and attentional control. For example, do neurons in the visual cortex show different activity patterns when the mice actively pay attention to the
stimuli compared to passive viewing? Since passive sessions may also include novel stimuli, researchers can investigate whether the processing of novelty happens
automatically or depends on attention and behavior. Also, passive sessions serve as a control to ensure that observed effects are not solely due to behavior or
rewards.  Such controls are critical to disentangle neural responses caused by external stimuli from those influenced by internal states such as motivation, attention,
or even fatigue.

## Data Structure & Terminology
Lastly, certain terminologies are important for understanding the dataset. A session is a continuous recording of neural activity and behavior. During a session, both
neural activity (via 2-photon calcium imaging) and the behavior of the mouse (such as licking to obtain rewards) are recorded. A maximum of one session is recorded per
mouse per day.
An experiment refers to a single imaging plane within a session. In single-plane imaging, only one imaging plane (= in the visual cortex) is studied in a session. In
this case, there is only one experiment per session. In multi-plane imaging, neural activity is measured simultaneously across up to 8 different imaging planes within
the visual cortex during a session. Each plane is considered a separate experiment. A multi-plane setup allows a larger volume of the brain to be captured in a single
session.
A container is the collection of all sessions (over multiple days) that relate to the same imaging plane (e.g., a specific layer of the visual cortex). A container
represents the same population of neurons recorded repeatedly over multiple days. This repeated measurement strategy provides a valuable dataset for understanding
longitudinal changes in neural activity, such as plasticity or stability, over time.

~ 50 full text rows