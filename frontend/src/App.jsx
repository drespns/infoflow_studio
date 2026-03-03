import { useState, useCallback } from "react";
import ReactFlow, {
  addEdge,
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState
} from "reactflow";
import "reactflow/dist/style.css";
import axios from "axios";

export default function App() {

  /**
   * Ruta del archivo subido.
   * Se usará en el LoadCSVNode.
   */
  const [uploadedPath, setUploadedPath] = useState(null);

  /**
   * Estados profesionales de React Flow.
   * useNodesState y useEdgesState permiten:
   * - mover nodos
   * - borrar nodos
   * - actualizar estado correctamente
   */
  const [nodes, setNodes, onNodesChange] = useNodesState([
    {
      id: "load1",
      position: { x: 100, y: 100 },
      data: { label: "Load CSV" },
      type: "default"
    },
    {
      id: "filter1",
      position: { x: 400, y: 100 },
      data: { label: "Filter Rows" },
      type: "default"
    }
  ]);

  const [edges, setEdges, onEdgesChange] = useEdgesState([
    { id: "e1", source: "load1", target: "filter1" }
  ]);

  /**
   * Resultado del pipeline.
   */
  const [result, setResult] = useState(null);

  /**
   * Maneja nuevas conexiones entre nodos.
   */
  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    []
  );

  /**
   * Sube archivo CSV al backend.
   */
  const uploadFile = async (file) => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setUploadedPath(response.data.path);
      alert("Archivo subido correctamente");

    } catch (error) {
      console.error(error.response?.data || error);
      alert(error.response?.data?.detail || "Error subiendo archivo");
    }
  };

  /**
   * Construye el JSON del pipeline
   * y lo envía al backend para ejecución.
   */
  const executePipeline = async () => {

    if (!uploadedPath) {
      alert("Debes subir un CSV primero.");
      return;
    }

    const pipelineJSON = {
      nodes: [
        {
          id: "load1",
          type: "load_csv",
          config: { path: uploadedPath }
        },
        {
          id: "filter1",
          type: "filter_rows",
          config: {
            column: "age",
            operator: ">",
            value: 30
          }
        }
      ],
      edges: edges.map(e => ({
        source: e.source,
        target: e.target
      })),
      target: "filter1"
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/execute",
        pipelineJSON
      );

      setResult(response.data.data);

    } catch (error) {
      console.error(error.response?.data || error);
      alert(error.response?.data?.detail || "Error ejecutando pipeline");
    }
  };

  return (
    <div className="w-screen h-screen flex">

      {/* Canvas principal */}
      <div className="w-3/4 h-full">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onConnect={onConnect}
          fitView
        >
          <MiniMap />
          <Controls />
          <Background />
        </ReactFlow>
      </div>

      {/* Panel lateral */}
      <div className="w-1/4 p-4 bg-gray-100 overflow-auto">

        <input
          type="file"
          accept=".csv"
          onChange={(e) => uploadFile(e.target.files[0])}
          className="mb-4"
        />

        <button
          onClick={executePipeline}
          className="bg-blue-600 text-white px-4 py-2 rounded w-full"
        >
          Ejecutar Pipeline
        </button>

        {result && (
          <div className="mt-4">
            <h2 className="font-bold mb-2">Resultado:</h2>
            <pre className="text-xs bg-white p-2 rounded max-h-64 overflow-auto">
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}