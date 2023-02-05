Vagrant.configure("2") do |config|
    
    config.vm.define "dashServer" do |ds|
        ds.vm.box = "ubuntu/kinetic64"
        ds.vm.hostname = "dashServer"
        ds.vm.network "private_network", ip: "192.168.50.50", mac: "080027000000",
            virtualbox__intnet: "ds-lg"
        ds.vm.provider "virtualbox" do |v|
            v.memory = 512
            v.cpus = 1
        end
        ds.vm.provision "ansible" do |ansible| 
            ansible.playbook = "conf/dash.yml"
        end
    end


    config.vm.define "videoClient" do |vc|
        vc.vm.box = "leandrocalmeida/xubuntu-vlc"
        vc.vm.hostname = "videoClient"
        vc.vm.network "private_network", ip: "192.168.50.51", mac: "080027000001",
            virtualbox__intnet: "ds-lg"
        vc.vm.provider "virtualbox" do |v|
            v.memory = 8192
            v.cpus = 8
            v.customize ["modifyvm", :id, "--accelerate3d", "on"]
            v.customize ["modifyvm", :id, "--vrde", "on"]
            v.customize ["modifyvm", :id, "--vrdeport", "8080"]

        end
        vc.vm.provision "ansible" do |ansible| 
            ansible.playbook = "conf/loadGen.yml"
        end
        #config.ssh.forward_x11 = true
    end
end