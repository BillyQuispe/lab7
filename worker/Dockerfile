# Build stage
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /app

# Copiar los archivos del proyecto
COPY *.csproj ./
RUN dotnet restore

# Copiar el código fuente
COPY . ./
RUN dotnet publish -c Release -o /out

# Runtime stage
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /app

# Copiar los archivos de salida del build
COPY --from=build /out .

# Comando de ejecución
ENTRYPOINT ["dotnet", "Worker.dll"]
