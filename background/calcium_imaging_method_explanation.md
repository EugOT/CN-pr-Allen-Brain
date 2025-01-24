# 2-Photon Calcium Imaging
Based on:
- Technical white paper: https://portal.brain-map.org/circuits-behavior/visual-behavior-2p
- Paper "Two-photon calcium imaging of neuronal activity": https://www.nature.com/articles/s43586-022-00147-1

To measure the activity of neurons in mice, the experiment used a technique called the 2-photon calcium imaging method. This method relies on special fluorescent dyes
or genetically modified molecules (such as the molecule GCaMP6 used in this experiment) that react to calcium. But why calcium? When a neuron "fires" (= becomes
active), calcium flows into the cell. By measuring the calcium levels, scientists can determine when and how strongly a neuron is active. With 2-photon calcium imaging,
researchers can precisely observe how individual neurons and larger networks respond to visual stimuli—in real-time. When combined with the Change Detection Task, this
method allows scientists to study how the brain processes environmental changes and how learning, novelty, and attention influence neuronal activity.

## Applications
2-Photon Caclium Imaging is widely used to study how networks of neurons function in tasks like processing sensory signals, controlling movements, storing memories, and
triggering emotions. For example, researchers have used 2-Photon Caclium Imaging to understand how neurons in the somatosensory cortex process touch and adapt to
changes like whisker plucking in mice. The technique is also valuable for linking neural activity to behaviors in awake animals (such as the detection task in this
experiment), including tracking changes in the brain during learning tasks. Beyond mice, 2-Photon Caclium Imaging is applied to other species like zebrafish and fruit
flies, where genetic tools make it easier to study neural activity in transparent and small organisms. 2-Photon Caclium Imaging is extensively used in disease research,
shedding light on different conditions. It has revealed altered brain activity in autism models, linked neuronal dysfunction to amyloid plaques in Alzheimer’s, and
studied recovery mechanisms after stroke. In addition, the technique is being explored in psychiatric disorders, such as depression and anxiety, to identify patterns of
hyper- or hypoactivity in specific brain regions, providing potential targets for therapies. Lastly, 2-Photon Caclium Imaging isn’t limited to neurons—it is used to
study calcium signals in non-neuronal cells like astrocytes, microglia, and retinal glia. These applications demonstrate 2-Photon Caclium Imaging versatility in
advancing our understanding of the brain and its disorders.

## Procedure in detail in the Experiment
The mice used in the experiment were genetically modified to produce a fluorescent protein called GCaMP6 in their neurons. This protein reacts to calcium by lighting up
when calcium enters the neurons. To observe this process, a small window (known as a cranial window) was surgically installed in the skull of the mouse, allowing the
microscope to visualize the brain tissue. To ensure accurate and stable measurements, the mouse was placed in a head-fixation system. This prevented movement from
disrupting the images and allowed precise alignment of the microscope. The head-fixation system is critical for maintaining stable imaging over extended recording
sessions, especially when analyzing neural activity patterns during complex behavioral tasks.
The key to this method is fluorescence, a physical phenomenon where molecules emit light of a specific wavelength when excited by light of a higher energy. In this
case, the fluorescent calcium indicator (= GCaMP6) reacts specifically to calcium. When calcium flows into a neuron (typically associated with neuronal activity), the
indicator's structure changes, increasing the brightness of the fluorescent signal and making neuronal activity visible.
To make the calcium indicator glow, it needs to be excited with light. In a 2-photon microscope, this is done using an infrared laser. Infrared light has a longer
wavelength (= lower energy) and penetrates deeper into tissue without causing damage. The laser can also focus on a very small region of the brain, where enough photons
meet simultaneously to trigger the fluorescence process. This approach avoids unnecessary illumination or damage to surrounding tissue. The laser scans rapidly across
the region of interest in the brain (known as scanning) and can operate in two main modes:
- Single-plane imaging, where only one thin layer of the visual cortex (a specific layer) is examined. The laser and camera focus on a fixed height, capturing activity
only in that plane. This provides highly detailed measurements of individual cells in a specific layer but does not provide information about other layers or larger
networks.
- Multi-plane imaging, where activity in multiple layers is measured simultaneously. This is achieved using a customized microscope system that can image up to eight
layers of the visual cortex at once. The laser moves quickly between the different planes, allowing measurements from various depths in a short time. This approach
enables researchers to analyze neuronal activity in a larger brain volume and study connections between layers, although the precision for individual layers may be
slightly reduced because the laser must switch between them.

The combined use of these imaging modes offers a flexible approach to studying neural circuits, from single-cell resolution to interactions across entire cortical
networks. 
The activity of each neuron is stored as a series of fluorescence data over time. These time-series data show how calcium concentration (and thus neuronal activity)
changes over time. Each image is synchronized with behavioral data, such as whether the mouse is licking or not. In multi-plane experiments, the data from each layer
are stored separately but can be analyzed together to provide insights into activity across the entire volume.

## Limitations
The 2-photon calcium imaging method has several advantages, such as the ability to measure neuronal activity without damaging surrounding tissue. However, it also has
some limitations. The results depend heavily on the quality of the preparation. Problems such as insufficient expression of the fluorescent molecule, motion artifacts,
or statistical noise can distort the data. Detecting individual action potentials (= spikes) is challenging, especially in inhibitory neurons or rapidly firing cells.
Another limitation is the relatively slow dynamics of calcium indicators compared to the actual speed of action potentials. While these indicators provide excellent
spatial resolution, their temporal resolution may miss very rapid firing events or lead to imprecise timing estimates for neural activity. Advances in imaging speed and
the development of more sensitive calcium indicators are needed to address these challenges. Additionally, light scattering limits the ability to study deeper brain
structures. Conventional 2-photon microscopes are not suitable for freely moving animals. However, improvements in portable 2-photon microscopes could help address this
limitation in the future and improve the stability of results. Finally, the large and complex datasets generated by this method make analysis slow. Real-time data
processing during experiments is necessary to dynamically adjust experimental settings and enable faster insights.

~ 50 full text rows