import torch
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(
        self,
        map,
        args,
        use_batch_norm: bool = True,
        use_layer_norm: bool = False,
        bias: bool = True,
        dropout_rate: float = 0.1,
        use_activation: bool = True,
        activation_fn: nn.Module = nn.ReLU
    ):
        super().__init__()
        self.method = "MLP"
        self.map = map
        self.args = args
        if self.map.shape[0] == 2:
            units = list(self.map.to_numpy()[0])
            units[0] = self.args.num_node_features
            self.units = units
        else:
            units = list(self.map.nunique())
            units[0] = self.args.num_node_features
            self.units = units
        self.use_batch_norm = use_batch_norm
        self.use_layer_norm = use_layer_norm
        self.bias = bias
        self.dropout_rate = dropout_rate
        self.use_activation = use_activation
        self.activation_fn = activation_fn
        # self.layers = nn.Sequential(
        #     collections.OrderedDict(
        #         [
        #             (
        #                 str(name),
        #                 nn.Sequential(
        #                     nn.Linear(
        #                         self.units[i],
        #                         self.units[i+1],
        #                         bias= self.bias,
        #                     ),
        #                     # non-default params come from defaults in original Tensorflow implementation
        #                     # nn.BatchNorm1d(self.units[i+1], momentum=0.01, eps=0.001)
        #                     # if self.use_batch_norm
        #                     # else None,
        #                     # nn.LayerNorm(self.units[i+1], elementwise_affine=False)
        #                     # if self.use_layer_norm
        #                     # else None,
        #                     self.activation_fn() if self.use_activation else None,
        #                     nn.Dropout(p=self.dropout_rate) if self.dropout_rate > 0 else None,
        #                 ),
        #             )
        #             for name, i in zip(map.keys(), range(len(self.units)-1))
        #         ]
        #     )
        # )
        self.modules = [
                        nn.Sequential(
                            nn.Linear(
                                self.units[i],
                                self.units[i+1],
                                bias= self.bias,
                            ),
                            # non-default params come from defaults in original Tensorflow implementation
                            nn.BatchNorm1d(self.units[i+1], momentum=0.01, eps=0.001)
                            # if self.use_batch_norm
                            # else None,
                            # nn.LayerNorm(self.units[i+1], elementwise_affine=False)
                            # if self.use_layer_norm
                            # else None,
                            # self.activation_fn() if self.use_activation else None,
                            # nn.Dropout(p=self.dropout_rate) if self.dropout_rate > 0 else None,
                        )
                    for name, i in zip(self.map.keys(), range(len(self.units)-1))
                ]
        self.modules.append(nn.Sequential(nn.Linear(self.units[-1], self.args.num_classes, bias = self.bias)))
        self.layers = nn.Sequential(*self.modules)
    
    def forward(self, data):
        x = data.x
        for i, layers in enumerate(self.layers):
            for layer in layers:
                x = F.relu(layer(x))
        return x