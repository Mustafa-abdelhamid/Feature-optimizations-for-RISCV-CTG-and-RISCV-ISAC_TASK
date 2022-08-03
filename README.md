# Feature-optimizations-for-RISCV-CTG-and-RISCV-ISAC_TASK
Coding challenge for LFX mentorship program
## Introduction 
It takes a valid RISC-V ISA string and generates coverpoints for each of the relevant bits in the extension field of misa register 

## Supported RISC-V string is:
* Valid riscv string 
* case insenstive 
* Can have underscores for readability 
(Extension version number isn't supported)
### Examples for Valid riscv ISA
```
RV32IMF
RV32EF
RV64I_Q
```
## Getting Started 
``` 
git clone https://github.com/Mustafa-abdelhamid/Feature-optimizations-for-RISCV-CTG-and-RISCV-ISAC_TASK.git

```
Then run the program with the desired RISV string  (RV32IMQ for example)
```
python3 main.py RV32IMQ
```
A YAML file containing Coverpoint is then Generated 

![image](https://user-images.githubusercontent.com/90484856/182505699-6df5af7d-87dd-429b-9230-3754ae4ba22b.png)
